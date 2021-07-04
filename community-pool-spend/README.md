# Osmosis and the Community Pool

Osmosis launched with community-spend capabilities, allowing OSMO stakers to vote to approve spending from the Community Pool. **This documentation is in active development, so please seek feedback and take care when using this information.** [Discuss its development here](https://forum.cosmos.network/t/gwg-community-spend-best-practices/3240).

## Why create a proposal to use Community Pool funds?

There are other funding options, most notably the Interchain Foundation's grant program. Why create a community-spend proposal?

**As a strategy: you can do both.** You can submit your proposal to the Interchain Foundation, but also consider submitting your proposal publicly on-chain. If Osmosis votes in favour, you can withdraw your Interchain Foundation application.

**As a strategy: funding is fast.** Besides the time it takes to push your proposal on-chain, the only other limiting factor is a fixed 3-day voting period. As soon as the proposal passes, your account will be credited the full amount of your proposal request.

**To build rapport.** Engaging publicly with the community is the opportunity to develop relationships with stakeholders and to educate them about the importance of your work. Unforeseen partnerships could arise, and overall the community may value your work more if they are involved as stakeholders.

**To be more independent.** The Interchain Foundation (ICF) may not always be able to fund work. Having a more consistently funded source and having a report with its stakeholders means you can use your rapport to have confidence in your ability to secure funding without having to be dependent upon the ICF alone.

## Drafting a Community-spend Proposal

Drafting and submitting a proposal is a process that takes time, attention, and involves risk. The objective of this documentation is to make this process easier by preparing participants for what to pay attention to, the information that should be considered in a proposal, and how to reduce the risk of losing deposits. Ideally, a proposal should only fail to pass because the voters 1) are aware and engaged and 2) are able to make an informed decision to vote down the proposal.

If you are considering drafting a proposal, you should review the general
background on drafting and submitting a proposal:
1. [How the voting process and governance mechanism works](/overview.md)
1. [How to draft your proposal and engage with the Cosmos community about it](/best_practices.md)
1. [How to submit your proposal](/submitting.md)

You should also review details specific to Community Pool Spend proposals:

1. [About the Community Pool](#learn-about-the-community-pool)
1. [Best practices for a Community Spend Proposal](best_practices.md)
1. [How to format Community Spend Proposals](formatting.md)

## Learn About the Community Pool

### What is the balance of the Community Pool?
You may directly query any Osmosis full node for the balance of the Community Pool:

```osmosisd q distribution community-pool --chain-id osmosis-1 --node osmosis-node-1.figment.network:26657```

Alternatively, the Osmosis explorers such as [Big Dipper](https://osmosis.bigdipper.live).

### How can funds from the Community Pool be spent?

Funds from the Osmosis Community Pool may be spent via successful governance proposal.

### How should funds from the Community Pool be spent?

We don't know 🤷

The prevailing assumption is that funds should be spent in a way that brings value to Osmosis.
However the community norms here are being actively formed by stakers today!

### How are funds disbursed after a community-spend proposal is passed?

If a community-spend proposal passes successfully, the number of OSMO encoded in the proposal will be transferred from the community pool to the address encoded in the proposal, and this will happen immediately after the voting period ends.
