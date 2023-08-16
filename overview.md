# The Proposal Process & Governance Mechanism

## The Proposal Process: Two Periods

### 1. Deposit Period

The deposit period lasts either 14 days or until the proposal deposit totals 1600 OSMOs, whichever happens first.

#### Deposits
Deposit amounts are at risk of being burned. Prior to a governance proposal entering the voting period (ie. for the proposal to be voted upon), there must be at least a minimum number of OSMOs deposited (1600). Anyone may contribute to this deposit. Deposits of passed and failed proposals are returned to the contributors.

In the past, different people have considered contributions amounts differently. There is some consensus that this should be a personal choice. There is also some consensus that this can be an opportunity for supporters to signal their support by adding to the deposit amount, so a proposer may choose to leave contribution room (ie. a deposit below 1600 OSMOs) so that others may participate. It is important to remember that any contributed OSMOs are at risk of being burned.

#### Burned deposits
Deposits are burned when proposals:
1. **Expire** - deposits will be burned if the deposit period ends before reaching the minimum deposit (1600 OSMO)
2. **Fail** to reach quorum - deposits will be burned for proposals that do not reach quorum ie. 30% of all staked OSMO must vote
3. **Are vetoed** - deposits for proposals with 33.4% of voting power backing the 'no-with-veto' option are also burned

### 2. Voting Period
The voting period is currently a fixed 3-day period. During the voting period, participants may select a vote of either 'yes', 'no', 'abstain', or 'no-with-veto'. Voters may change their vote at any time before the voting period ends.

## What determines whether or not a governance proposal passes?
There are four criteria:

1. A minimum deposit of 1600 OSMO is required for the proposal to enter the voting period
   - anyone may contribute to this deposit
   - the deposit must be reached within 14 days (this is the deposit period)
2. A minimum of 30% of the network's voting power (quorum) is required to participate to make the proposal valid
3. A simple majority (greater than 50%) of the participating voting power must back the 'yes' vote during the 14-day voting period
4. Less than 33.4% of participating voting power votes 'no-with-veto'

Currently, the criteria for submitting and passing/failing all proposal types is the same. 

### How is voting tallied?
Voting power is determined by stake weight at the end of the 3-day voting period and is proportional to the number of total OSMOs participating in the vote. Only bonded OSMOs count towards the voting power for a governance proposal. Liquid OSMOs will not count toward a vote or quorum.

Inactive validators can cast a vote, but their voting power (including the backing of their delegators) will not count toward the vote if they are not in the active set when the voting period ends. That means that if I delegate to a validator that is either jailed, tombstoned, or ranked lower than 100 in stake-backing at the time that the voting period ends, my stake-weight will not count in the vote.

Though a simple majority 'yes' vote (ie. 50% of participating voting power) is required for a governance proposal vote to pass, a 'no-with-veto' vote of 33.4% of participating voting power or greater can override this outcome and cause the proposal to fail. This enables a minority group representing greater than 1/3 of voting power to fail a proposal that would otherwise pass.

### How is quorum determined?

Voting power, whether backing a vote of 'yes', 'abstain', 'no', or 'no-with-veto', counts toward quorum. Quorum is required for the outcome of a governance proposal vote to be considered valid and for deposit contributors to recover their deposit amounts. If the proposal vote does not reach quorum (ie. less than 40% of the network's voting power is participating) within 14 days, any deposit amounts will be burned and the proposal outcome will not be considered to be valid.
