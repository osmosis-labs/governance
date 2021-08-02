# Fix prop 6 ratios

**Quick Summary of issue**

Proposal 6, a proposal that got passed offering a change in incentives distributions in order to include Regen, had a data entry error that differed from the proposal text.
This error went uncaught in the governance approval process, and was approved and included on chain.

Proposal 6 was passed in the last epoch. This proposal offers a governance proposal to align the ratios with what was proposed in proposal 6, except with the following modification:
* The Community pool allocation is lowered from 5% to 1%, with that remaining 4% being distributed evenly across all pools with lower than expected allocations per the text of prop 6.
This is namely every incentivized pool, except for the OSMO/ION, ATOM/REGEN, and OSMO/REGEN pools.

## Proposal title

Correct the ratios for Prop 6, with lowering of the community pool incentives

## Proposal Description

Proposal 6, a proposal that got passed offering a change in incentives distributions in order to include Regen pools, had a data entry error that differed from the proposal text.
This error went uncaught in the governance approval process, and was approved and included on chain.
This highlights the need for more tooling and standards being set here for ensuring that
any manual adjustments to OSMO pool incentives get much more auditability.

Proposal 6 was passed in the last epoch at the time of this proposal's writing. This proposal offers a governance proposal to align the ratios with what was proposed in proposal 6, except with the following modification:

The Community pool allocation is lowered from 5% to 1%, with the remaining 4% being distributed evenly across all pools with lower than expected allocations per the text of prop 6.
This is namely every incentivized pool, except for the OSMO/ION, ATOM/REGEN, and OSMO/REGEN.
This is done as a means of accounting for the lower than expected rewards in the interrim.

Alternatively the community could equally vote on a new incentives distribution, such as is proposed in proposal 8, or a new proposal based on current TVL similar to proposal 2.
One important thing to remark is that it is plausible that this proposal and proposal 8 both enter their voting period during the same epoch. If this is the case, only one should be voted yes. (As whichever one gets passed second will override the other within the same epoch)

The intended distribution after proposal 6 (per the proposer's understanding):
```
Community pool 5%
ATOM/OSMO 21.77%
ION/OSMO 2.00%
AKT/OSMO 10.89%
AKT/ATOM 10.89%
DVPN/OSMO 6.53%
DVPN/ATOM 6.53%
IRIS/OSMO 1.74%
IRIS/ATOM 1.74%
CRO/OSMO 1.74%
CRO/ATOM 1.74%
XPRT/OSMO 8.71%
XPRT/ATOM 8.71%
REGEN/OSMO 6.00%
REGEN/ATOM 6.00%
```

This proposal proposes the following (the distribution of 4% from the community pool to non-ION/Regen pools). You derive these numbers by taking the numbers from before, and for non-regen/ion pools, multiplying them by (1 + `.04/.81`). This is reasoned as distributing `4%` across what was previously `81%` of the total amount. More decimal points of precision were used for the prior numbers, the following numbers are rounded.

```
Community pool 1%
pool 1 ATOM/OSMO 22.84%
pool 2 ION/OSMO 2.00%
pool 3 AKT/OSMO 11.42%
pool 4 AKT/ATOM 11.42%
pool 5 DVPN/OSMO 6.86%
pool 6 DVPN/ATOM 6.86%
pool 7 IRIS/OSMO 1.83%
pool 8 IRIS/ATOM 1.83%
pool 9 CRO/OSMO 1.83%
pool 10 CRO/ATOM 1.83%
pool 13 XPRT/OSMO 9.14%
pool 15 XPRT/ATOM 9.14%
pool 22 REGEN/OSMO 6.00%
pool 42 REGEN/ATOM 6.00%
```

Prop 6 proposed that these be split across lockup lengths by 80% to 1 day, 15% to 7 days, 5% to 14 days.
We propose resetting the total number of allocation points to 1 million for simplicity, and using
the exact percentages from above.

Then, this parameter change is encoded via the following gauge allocation points (annotated)

```
Community Pool: 10000
pool 1 ATOM/OSMO gauges 1,2,3: 182720,34260,11420
pool 2 ION/OSMO gauges 4,5,6: 16000,3000,1000
pool 3 AKT/OSMO gauges 7,8,9: 91360,17130,5710
pool 4 AKT/ATOM gauges 10,11,12: 91360,17130,5710
pool 5 DVPN/OSMO gauges 13,14,15: 54880,10290,3430
pool 6 DVPN/ATOM gauges 16,17,18: 54880,10290,3430
pool 7 IRIS/OSMO gauges 19,20,21: 14640,2745,915
pool 8 IRIS/ATOM gauges 22,23,24: 14640,2745,915
pool 9 CRO/OSMO gauges 25,26,27: 14640,2745,915
pool 10 CRO/ATOM gauges 28,29,30: 14640,2745,915
pool 13 XPRT/ATOM gauges 37,38,39: 73120,2745,915
pool 15 XPRT/OSMO gauges 43,44,45: 73120,2745,915
pool 22 REGEN/ATOM gauges 64,65,66: 48000,9000,3000
pool 42 REGEN/OSMO gauges 124,125,126: 48000,9000,3000
```

### How to check this

Check each step of the above derivation. (You can get the gauge ids for the last part by querying the gauge ID via `osmosisd query incentives gauge-by-id {number}`)

Then query the live proposal at `osmosisd query gov proposal {number}`, and check that the gauge/allocation point mapping is correct.

-- End of proposal description

## Command to make the proposal

See command.md
