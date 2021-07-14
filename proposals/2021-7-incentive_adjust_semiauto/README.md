
# Semi-Automatic model based incentive adjustments

## The Meta-Proposal

- Liquidity incentives have so far been set in an ad-hoc and error prone manner.

- We should create a predictable system for adjusting liquidity incentives according to a publicly known algorithm / model, designed to achieve some publicly agreed set of goals.

- We should commit to adjusting incentives slowly, so that liquidity providers don't have to worry about huge swings in returns happening faster than they can unbond / exit pools.

- We should utilize publicly visible computational tools to automate the calculation of gauge weights to be proposed.

- We should not (yet) create a fully automated system for adjusting liquidity incentives, so as to keep requiring governance approval for each adjustment, and to leave open the option to change the model as needed.

## The Proposed Model
### Motivations
- Interchain users want liquid pools to exchange IBC tokens.
- They also want the opportunity to hedge and earn yield by providing IBC tokens to pools.
- We (OSMO holders) want OSMO pools to capture trading volume, and to be used as the base pair when hedging or yield farming with an IBC token.
- We use Liquidity incentives to steer capital into pools.
### Definition:
  - "Relative Liquidity" := TVL / Volume.
    - Assume 7Day Volume in everything that follows.
    - Higher relative liquidity means lower price slippage as a result of normal trading.
### Claim 1: The most efficient state of the market is for major pools to have approximately the same relative liquidity
  - Ie, the amount of TVL in each pool is proportional to the amount of volume transacting through it, with a common proportion between pools.
  - Such that, no matter which trading pair you look at, the average slippage as a result of normal trading is of the same relative magnitude.
  - This minimizes the expected slippage for the average user / average trade.
### Claim 2: It is beneficial to OSMO holders if pools with an OSMO pair have better relative liquidity than their corresponding ATOM pools
  - For a trade of ATOM->X, at some trade size, it should be cheaper (lower fees + slippage) to trade through ATOM->OSMO->X than to trade directly through the ATOM pool.
  - Likewise, for a trade of X->Y, it should be cheaper to use X->OSMO->Y, than X->ATOM->Y.
  - This will mean that OSMO bonded into pools will be capturing swap fees
  - This will also mean that reinvestment of incentive rewards will create less downward price pressure on OSMO.
    - ie people selling half their OSMO for X to LP and bond in X/OSMO, rather than selling half for X and half for ATOMS to LP in the X/ATOM pool.

## The Proposed Adjustment Algorithm
- In concrete terms, the proposal is that we use this [spreadsheet](https://docs.google.com/spreadsheets/d/15-b7o4QHY4SNE7Cw6MSZZ9Xxxbwca_hw4coLN9Y2ZFM/edit?usp=sharing) , to automatically calculate adjustments to pool incentives according to the following model.
- Because of the delays required in the governance process, (deposit and voting time), we should pick a regular time each week, and if it has been at least a full 7 days of rewards under the previous accepted proposal, then we generate and propose the new one.
  - In the event that for some reason the previous proposal hasn't been in effect for a full 7 days, then we would simply wait until the next week to make the next adjustment proposal.
  - This would most likely lead to adjustments happening every 14 days. ie proposal on day 0, accepted after ~3-6 days, in effect for at least a full week and then next proposal on day 14.
### Proposal Process
  - Make a copy of the sheet, so that we have a record of the numbers used in the process.
  - Export the Gauges page to a csv file.
  - Run a script (to be written) to create and submit the governance proposal using data from columns `A` and `I` of the Gauges csv file.
    - Proposal should include a link to the spreadsheet copy used, so that voters can easily check the math as well as the validity of the input data.
### Data Flow of spreadsheet:
  - Data (TVL and Volume) is pulled from https://api-osmosis.imperator.co/search/v1/pools through the use of a [script](https://gist.github.com/UnityChaos/b6af1b8352416dfd4570048616218110) which currently runs automatically every hour.
  - We calculate the (7day) Relative Liquidity for each pool.
  - Relative Liquidity for each pool is "Biased" according to the `Bias` factor (currently 50%).
    - For a factor of 50%, this means that OSMO pools will target a Relative Liquidity 50% higher than average, and ATOM pools will target a value 50% lower.
    - For example, if average Relative Liquidity was 200%, we would be targeting OSMO pools at 300% and ATOM pools at 100%.
  - We divide the average Relative Liquidity (over all incentivized pools) by each pool's Biased Relative Liquidity to find the "Imbalance" factor.
  - We then take the current percentage share of liquidity incentives going to each pool, and adjust them by multiplying by the Imbalance factor passed through a modified Logit function.
    - This function maps Imbalance values to adjustments, which are bounded by the `Scale` factor(currently 10%), and have the property that small Imbalances (between 50% and 150%) are mapped to smaller adjustments.
      - For example, so that a pool with an Imbalance factor of 105% would be adjusted by 0.44% rather than a full 5%.
  - After adjustment, the share percentages have to be renormalized so that their sum matches what it was before.
    - Currently liquidity incentives sum up to 99%, because 1% is going to the community pool.
    - This renormalization can lead to some adjustments being larger than the scale factor.
      - For example if the scale factor is 10%, and many pools are being reduced by 10%, that reduction in total percentage will be redistributed back to all pools, and some that were being increased by 10% will go above the scale factor.
  - These renormalized percentages are then used to automatically derive new Gauge weights. This is what will actually be proposed on chain.
    - Desired total gauge weight for each pool is taken to be the pool's desired share of incentives multiplied by 1,000,000, and then rounded
    - These total gauge weights for each pool are then split into gauges for each time scale. With the 1 day getting 80%, the 7 day 15%, and the 14 day getting 5%. These are also rounded.
    - The total gauge weights of each pool and of all together are summed up again to factor in any small effects of rounding, and the final share percentages are derived.
    - These should generally match the "Desired Share" percentages to at least the first few decimal places.


## Limitations of this Model / Proposal
- Does not take account of correlations between X/OSMO and X/ATOM pools.
- Does not directly deal with the implications of redirecting X/ATOM trade through combination of X/OSMO and OSMO/ATOM. ie using two pools instead of one doubles the "volume" created by each trade.

## Open Questions
- How are we deciding eligibility for pool incentives?
  - So far we seem to have followed a process of roughly:
    -  "We incentivize the largest X/OSMO and X/ATOM pool which has non-zero swap fee"
  - Do we have a preference for particular pool weights?
    - Pools 1, 3, 5, 7, 9, 10, 13, 15, 22, and 42 are all 50/50
    - Pools 2, 4, 6 and 8 are not.
  - What about pools with more than 2 assets?
    - Would triple pools (OSMO/ATOM/X) for each token X be a good compromise. Where it's possible to directly trade Atom/X, but where rewards are linked to OSMO exposure?
    - What about "one big pool" with all the assets?
      - This could be market cap weighted to make a diversified index fund.
- How do we decide the share of incentives a new pool should get?
  - The relative liquidity model cannot tell us a correct starting incentive share, it only gives adjustments relative to current amounts.
  - A reasonable option might be to select a starting share which would give the pool an APR equal to the TVL weighted average of existing pools.