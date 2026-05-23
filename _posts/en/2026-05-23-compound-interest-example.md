---
typora-root-url: ../
layout: single
title: >
  Compound Interest Example: How Money Grows on Money
seo_title: >
  Compound Interest Example: How Money Grows on Money
date: 2026-05-23T23:40:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: en
translation_id: compound-interest-example
header:
   teaser: /images/2026-05-23-compound-interest-example/compound-interest-hero.png
   overlay_image: /images/2026-05-23-compound-interest-example/compound-interest-hero.png
   overlay_filter: 0.35
   image_description: >
     Visual guide explaining Compound Interest Example: How Money Grows on Money.
excerpt: >
  Understand compound interest with simple numbers, a reusable formula, a year-by-year table, and common mistakes about returns, deposits, taxes, and inflation.
seo_description: >
  Understand compound interest with simple numbers, a reusable formula, a year-by-year table, and common mistakes about returns, deposits, taxes, and inflation.
categories:
  - en_Economy
tags:
  - Economy
  - Finance
  - CompoundInterest
  - Investing
  - Budgeting
---

## Quick Answer

Compound interest means earning interest on your original money and on the interest that has already been added.
If you start with $1,000 and earn 5% once per year, the first year adds $50.
The second year earns 5% on $1,050, so the interest is $52.50.
That small difference grows as time gets longer.

![Compound interest growth shown with stacked coins and a rising curve](/images/2026-05-23-compound-interest-example/compound-interest-hero.png)

The image shows the core idea: the base amount grows, then the next return is calculated on a larger base.
This article is educational, not investment advice.
Actual returns can be lower, higher, or negative, and taxes, fees, inflation, and risk matter.

## The Basic Formula

For a one-time deposit with no additional contribution, the standard compound interest formula is:

```text
A = P(1 + r/n)^(nt)
```

Where:

- `A` is the final amount.
- `P` is the starting principal.
- `r` is the annual interest rate as a decimal.
- `n` is the number of compounding periods per year.
- `t` is the number of years.

If interest is compounded once per year, `n = 1`.
The formula becomes:

```text
A = P(1 + r)^t
```

For a simple first example:

```text
P = 1,000
r = 0.05
t = 10

A = 1,000 x (1.05)^10
A = 1,628.89
```

After 10 years, $1,000 becomes about $1,628.89 at 5% annual compounding.
The gain is about $628.89.

## Year-by-Year Example

Here is the same example without hiding the steps.

| Year | Starting balance | 5% interest | Ending balance |
| ---: | ---: | ---: | ---: |
| 0 | $1,000.00 | - | $1,000.00 |
| 1 | $1,000.00 | $50.00 | $1,050.00 |
| 2 | $1,050.00 | $52.50 | $1,102.50 |
| 3 | $1,102.50 | $55.13 | $1,157.63 |
| 4 | $1,157.63 | $57.88 | $1,215.51 |
| 5 | $1,215.51 | $60.78 | $1,276.28 |
| 10 | - | - | about $1,628.89 |

The interest amount gets larger because the balance gets larger.
That is the part people mean when they say "interest on interest".

## Simple Interest vs Compound Interest

Simple interest earns on the original principal only.
Compound interest earns on the principal plus accumulated interest.

Using the same $1,000 and 5% for 10 years:

```text
Simple interest:
1,000 + (1,000 x 0.05 x 10) = 1,500

Compound interest:
1,000 x (1.05)^10 = 1,628.89
```

The difference is $128.89 in this small example.
The difference becomes much larger with more time, higher rates, or repeated contributions.

## Why Time Matters So Much

Compound growth is slow at first.
Then the gap becomes easier to see.

With $1,000 at 5% annual compounding:

| Time | Approximate balance |
| ---: | ---: |
| 5 years | $1,276 |
| 10 years | $1,629 |
| 20 years | $2,653 |
| 30 years | $4,322 |

Nothing magical happens in year 20 or 30.
The formula is the same.
The later years simply start from a larger base.

This is why saving early can matter.
It gives compounding more time to work.
But time alone is not enough.
The rate, risk, fees, taxes, and whether you keep contributing all change the result.

## Example with Monthly Contributions

Most people do not invest one lump sum and then stop.
They add money over time.

Suppose:

```text
Starting amount: $1,000
Monthly contribution: $100
Annual return assumption: 5%
Time: 10 years
```

The result is not just the original $1,000 compounding.
Every monthly contribution also has time to grow.
Earlier contributions grow longer than later contributions.

That is why a calculator is helpful.
Investor.gov provides a compound interest calculator where you can change starting amount, monthly contribution, time, rate, and compounding frequency.

Use calculators for scenarios, not promises.
If you enter 8%, the calculator does not guarantee 8%.
It only shows what would happen if that assumption came true.

## The Rule of 72

The Rule of 72 is a quick estimate for how long it takes money to double.

```text
Years to double = 72 / annual return rate
```

Examples:

| Assumed annual rate | Approximate doubling time |
| ---: | ---: |
| 3% | 24 years |
| 6% | 12 years |
| 8% | 9 years |
| 12% | 6 years |

This is only a rule of thumb.
It is useful for mental math, not exact planning.

## Common Mistakes

### Mistake 1: Treating Assumed Returns as Guaranteed

A bank savings rate, bond yield, and stock market return are not the same thing.
Some rates are stated in advance.
Market returns move and can be negative.

When writing a plan, label the number clearly:

```text
guaranteed rate
expected return
historical average
scenario assumption
```

Do not mix them.

### Mistake 2: Ignoring Inflation

If prices rise, the future balance buys less than the same number today.
A $10,000 future balance is not the same as $10,000 of current purchasing power.

For long-term planning, look at real return after inflation when possible.

### Mistake 3: Ignoring Taxes and Fees

Fees reduce the balance that can compound.
Taxes can reduce what you keep.
The gross return in a calculator can look much better than the after-fee, after-tax result.

### Mistake 4: Confusing Compound Interest with All Investing

The phrase compound interest is precise for interest-bearing accounts and debt.
Stock investing often compounds through reinvested dividends and business growth, but the return is not a fixed interest payment.
Use the broader phrase compound growth when discussing variable investments.

### Mistake 5: Waiting for a Perfect Amount

Compounding rewards time and consistency.
A small habit started early can beat a larger habit started much later.
That does not mean everyone should invest immediately in risky assets.
It means the time variable is powerful.

## A Reusable Spreadsheet Layout

You can model a simple annual example with these columns:

```text
Year
Starting balance
Contribution
Interest rate
Interest earned
Ending balance
```

Formula idea:

```text
Ending balance = (Starting balance + Contribution) x (1 + Interest rate)
```

For monthly models, use monthly periods.
Do not mix annual rates and monthly periods unless you convert the rate correctly.

## How to Use This in Real Life

Use compound interest examples for planning questions:

- How much could a monthly saving habit become?
- How much does delaying by five years change the result?
- How much do fees reduce the ending balance?
- What happens if the return is lower than expected?
- How much of the ending value comes from contributions vs growth?

The best use is comparison.
Run several conservative scenarios before making a decision.

## Related Reading

- [50/30/20 Budget Rule](/en_economy/household-budget-50-30-20/)
- [Interest Rates and Inflation Explained](/en_economy/interest-rate-inflation-basics/)
- [How Much Emergency Fund Do You Need](/en_economy/emergency-fund-how-much/)

## FAQ

### When should I use this guide?

Use it to understand a personal finance concept before making a budget, savings plan, or comparison. This article is educational and is not personal financial advice.

### What should beginners verify first?

Start by writing the assumptions: time horizon, cash flow, fees, taxes, inflation, and risk tolerance. The conclusion changes when those assumptions change.

### Which keywords should I search next?

Search for "Compound Interest Example: How Money Grows on Money" together with personal finance, interest rate, inflation, budget, risk, and calculator keywords.

## Sources

- Investor.gov, Compound Interest: https://www.investor.gov/index.php/introduction-investing/investing-basics/glossary/compound-interest
- Investor.gov, Financial Tools and Calculators: https://www.investor.gov/free-financial-planning-tools-0
- Federal Reserve Education, Simple and Compound Interest lesson: https://www.federalreserveeducation.org/teaching-resources/personal-finance/saving/simple-and-compound-interest-why-it-is-great-to-save-lesson-6b
- SEC student investing education, compound interest and Rule of 72: https://www.sec.gov/investor/students/tips.htm
