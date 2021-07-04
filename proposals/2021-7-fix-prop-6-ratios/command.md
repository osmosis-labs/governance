# Submitting the proposal

The intended full proposal description should be converted into an IPFS link or github permalink. A candidate full proposal description can be found in the ##Proposal Description section of the README.md.

Below we give a sample description with an IPFS link:

## Sample description

Proposal 6, a proposal that got passed offering a change in incentives distributions in order to include Regen pools, had a data entry error that differed from the proposal text. This error went uncaught in the governance approval process, and was approved and included on chain. This highlights the need for more tooling and standards being set here for ensuring that any manual adjustments to OSMO pool incentives get much more auditability.\n\nProposal 6 was passed in the last epoch at the time of this proposal's writing. This proposal offers a governance proposal to align the ratios with what was proposed in proposal 6, except with the following modification:\n\nThe Community pool allocation is lowered from 5% to 1%, with the remaining 4% being distributed evenly across all pools with lower than expected allocations per the text of prop 6.\nThis is namely every incentivized pool, except for the OSMO/ION, ATOM/REGEN, and OSMO/REGEN.\nThis is done as a means of accounting for the lower than expected rewards in the interrim.\n\nAlternatively the community could equally vote on a new incentives distribution, such as is proposed in proposal 8, or a new proposal based on current TVL similar to proposal 2.\n\n One important thing to remark is that it is plausible that this proposal and proposal 8 both enter their voting period during the same epoch. If this is the case, only one should be voted yes. (As whichever one gets passed second will override the other within the same epoch)\n IPFS link with full description of percentages and how to check the proposal: {URL to full description}

## Command

Below is a sample command that can be used to submit the proposal, with the title, description, node and from field still needing to be filled out.

```
osmosisd tx gov submit-proposal update-pool-incentives 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,37,38,39,43,44,45,64,65,66,124,125,126 10000,182720,34260,11420,16000,3000,1000,91360,17130,5710,91360,17130,5710,54880,10290,3430,54880,10290,3430,14640,2745,915,14640,2745,915,14640,2745,915,14640,2745,915,73120,13710,4570,73120,13710,4570,48000,9000,3000,48000,9000,3000 --title="{Title of your choosing}" --desc="Description with an IPFS/github link" --from={yourkey} --deposit=1uosmo --chain-id=osmosis-1 --node="tcp://{ip of a full node}:26657"
```
