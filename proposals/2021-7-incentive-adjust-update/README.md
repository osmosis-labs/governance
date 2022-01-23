
# Update to the Semi-Automatic Incentive Adjustments Model of Prop 13

## Overview

This model builds on the previous model with some improvements. The overall goal and methods remain largely the same.

## Spreadsheet
The spreadsheet implementing this model can be found here: https://docs.google.com/spreadsheets/d/12JQca-EPhdPuLmvO1nqiNQ8THEfffkLw-H9o05Ta3s8/edit?usp=sharing

## Changes

### Prop 13 Model
The old model is essentially computing the `TVL / (Bias_Factor * Volume)` ratio for each pool (where `ATOM` pools have a `Bias_Factor` of `50%`, and `OSMO` pools `150%`), and then comparing to the ratio across all pools to determine which are "overweight" or "underweight". If a pools ratio is higher than average, then it has "too much" liquidity and would have it's incentives lowered, and vice versa for below the average.

### New Model
Under the new model, the ratio is modified to `(TVL * (1 - OSMO_Share)) / (Swap_Fee * Volume)`. Compared to the Prop 13 model this can be seen as making two changes:

1. Using `Swap_Fee * Volume` instead of just `Volume`. This is primarily to address the concerns about potential manipulation. Volume can easily be artificially created, especially in low or no fee pools. For example in a pool with a swap fee of 0.3%, it only costs $3000 in fees to create $1,000,000 in volume. This also has the effect of incentivizing pools to set their swap fee to maximize fee revenue to the pool. Currently pools are unable to change their swap fees, but this will change when pools become self governing, and we should expect them to attempt to find the right level to maximize fee revenue.
2. Using `1 - OSMO_Share` in the numerator, instead of the `Bias_Factor` in the denominator. This is equivalent to using a consistent `Bias_Factor` for all pools, equal to `1/(1 - OSMO_Share)`. So for `ATOM` pools, they would change from `50%` to `100%`, and 50/50 `OSMO` pools would change from `150%` to `200%`, while pools like pool 2, with only 20% OSMO would change from `150%` to `125%`. This has the effect of scaling desired liquidity of a pool by it's OSMO Share, but without setting non-OSMO pools to zero.


The direct interpretation of this model is that "The percentage of total Non-OSMO value held by a pool should be equal to it's percentage of total swap fees collected". For example, if 20% of the swap fees were being collected by one pool, then that pool should be holding 20% of the Non-Osmo value in the system.

#### Minor Changes
  - The spreadsheet uses a new API from Imperator to pull historical TVL and Volume data for each pool, and compute the average TVL across the last 7 days and the total volume. Rather than what the old spreadsheet was doing, which was taking a live sample of the TVL and last 7 days of volume. This should make after the fact verification of the data used for an adjustment easier, as the historical values are retained in the API.
  - Fixed an approximation error in the math for the modified Logit function. Previously it was using `0.01` and `0.99` as bounds, which necessitated dividing the result by 2 to rescale, this is approximately correct but leads to an extra dampening effect. It has been switched to the "correct" bounds of `1/11` and `10/11`, after some math debugging with @ValarDragon.
