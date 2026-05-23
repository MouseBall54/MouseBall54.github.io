---
typora-root-url: ../
layout: single
title: >
  복리 계산 예시: 돈이 돈을 버는 구조를 숫자로 이해하기
seo_title: >
  복리 계산 예시: 돈이 돈을 버는 구조를 숫자로 이해하기
date: 2026-05-23T23:40:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: compound-interest-example
header:
   teaser: /images/2026-05-23-compound-interest-example/compound-interest-hero.png
   overlay_image: /images/2026-05-23-compound-interest-example/compound-interest-hero.png
   overlay_filter: 0.35
   image_description: >
     복리 계산 예시: 돈이 돈을 버는 구조를 숫자로 이해하기 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  복리 계산을 원금, 이자율, 기간, 재투자 구조로 나누어 보고, 단리와의 차이, Rule of 72, 세금과 물가를 함께 이해합니다.
seo_description: >
  복리 계산을 원금, 이자율, 기간, 재투자 구조로 나누어 보고, 단리와의 차이, Rule of 72, 세금과 물가를 함께 이해합니다.
categories:
  - ko_Economy
tags:
  - Economy
  - Finance
  - CompoundInterest
  - Investing
  - Budgeting
---

## 핵심 요약

복리는 처음 넣은 돈뿐 아니라 이미 붙은 이자에도 다시 이자가 붙는 구조입니다.
처음에 1,000달러를 넣고 1년에 5%를 받는다고 가정하면 첫해 이자는 50달러입니다.
둘째 해에는 1,050달러에 5%가 붙기 때문에 이자가 52.50달러가 됩니다.
작아 보이는 차이가 시간이 길어질수록 커집니다.

![동전 더미와 상승 곡선으로 표현한 복리 성장 이미지](/images/2026-05-23-compound-interest-example/compound-interest-hero.png)

이미지는 복리의 핵심을 보여줍니다.
기준 금액이 커지고, 다음 수익이 더 커진 기준 금액 위에서 계산됩니다.
이 글은 교육용 설명이며 투자 권유가 아닙니다.
실제 수익률은 낮거나 높거나 마이너스일 수 있고, 세금, 수수료, 물가, 위험도 함께 봐야 합니다.

## 기본 공식

추가 납입이 없는 한 번의 예치금이라면 복리 공식은 아래와 같습니다.

```text
A = P(1 + r/n)^(nt)
```

각 항목의 뜻:

- `A`: 최종 금액
- `P`: 시작 원금
- `r`: 연 이자율 또는 수익률을 소수로 바꾼 값
- `n`: 1년 동안 복리 계산이 이루어지는 횟수
- `t`: 기간, 단위는 년

1년에 한 번 복리 계산을 한다면 `n = 1`입니다.
공식은 더 단순해집니다.

```text
A = P(1 + r)^t
```

가장 간단한 예시는 다음과 같습니다.

```text
P = 1,000
r = 0.05
t = 10

A = 1,000 x (1.05)^10
A = 1,628.89
```

연 5% 복리로 10년이 지나면 1,000달러는 약 1,628.89달러가 됩니다.
증가분은 약 628.89달러입니다.

## 연도별 예시

같은 예시를 단계별로 보면 더 직관적입니다.

| Year | Starting balance | 5% interest | Ending balance |
| ---: | ---: | ---: | ---: |
| 0 | $1,000.00 | - | $1,000.00 |
| 1 | $1,000.00 | $50.00 | $1,050.00 |
| 2 | $1,050.00 | $52.50 | $1,102.50 |
| 3 | $1,102.50 | $55.13 | $1,157.63 |
| 4 | $1,157.63 | $57.88 | $1,215.51 |
| 5 | $1,215.51 | $60.78 | $1,276.28 |
| 10 | - | - | 약 $1,628.89 |

이자가 점점 커지는 이유는 balance가 커지기 때문입니다.
사람들이 "이자에 이자가 붙는다"고 말하는 부분이 바로 이것입니다.

## 단리와 복리의 차이

단리는 처음 원금에만 이자가 붙습니다.
복리는 원금과 지금까지 쌓인 이자에 다시 이자가 붙습니다.

같은 1,000달러, 5%, 10년을 비교하면 아래와 같습니다.

```text
단리:
1,000 + (1,000 x 0.05 x 10) = 1,500

복리:
1,000 x (1.05)^10 = 1,628.89
```

이 작은 예시에서도 차이는 128.89달러입니다.
기간이 길어지거나, 수익률이 높아지거나, 매달 추가 납입이 있으면 차이는 더 커집니다.

## 시간이 중요한 이유

복리 성장은 처음에는 느려 보입니다.
시간이 길어질수록 차이가 눈에 띄기 시작합니다.

1,000달러를 연 5% 복리로 둔다고 가정하면:

| 기간 | 대략적인 금액 |
| ---: | ---: |
| 5년 | $1,276 |
| 10년 | $1,629 |
| 20년 | $2,653 |
| 30년 | $4,322 |

20년이나 30년에 특별한 마법이 생기는 것은 아닙니다.
공식은 같습니다.
나중의 연도는 더 큰 금액에서 시작하기 때문에 증가분이 커지는 것입니다.

그래서 일찍 저축을 시작하는 것이 중요할 수 있습니다.
복리가 작동할 시간을 더 주기 때문입니다.
하지만 시간만으로 충분하지는 않습니다.
수익률, 위험, 수수료, 세금, 추가 납입 여부가 모두 결과를 바꿉니다.

## 매달 납입하는 경우

대부분의 사람은 한 번 돈을 넣고 끝내지 않습니다.
시간이 지나며 돈을 더 넣습니다.

예를 들어 아래처럼 가정해 봅니다.

```text
시작 금액: $1,000
월 납입액: $100
연 수익률 가정: 5%
기간: 10년
```

이 경우 결과는 처음 1,000달러만 복리로 불어나는 것이 아닙니다.
매달 넣는 돈도 각각 남은 기간만큼 성장합니다.
일찍 넣은 돈은 더 오래 성장하고, 늦게 넣은 돈은 성장 기간이 짧습니다.

그래서 calculator를 사용하는 것이 좋습니다.
Investor.gov의 compound interest calculator에서는 시작 금액, 월 납입액, 기간, 이자율, 복리 계산 주기를 바꿔볼 수 있습니다.

Calculator는 약속이 아니라 시나리오를 보여주는 도구입니다.
8%를 입력했다고 해서 8%가 보장되는 것은 아닙니다.
그 가정이 맞았을 때 어떤 결과가 나오는지 보여줄 뿐입니다.

## Rule of 72

Rule of 72는 돈이 두 배가 되는 시간을 빠르게 추정하는 방법입니다.

```text
두 배가 되는 데 걸리는 년수 = 72 / 연 수익률
```

예시:

| 가정한 연 수익률 | 대략적인 두 배 시간 |
| ---: | ---: |
| 3% | 24년 |
| 6% | 12년 |
| 8% | 9년 |
| 12% | 6년 |

이것은 정확한 계산이 아니라 mental math에 가까운 rule of thumb입니다.
대략적인 감을 잡는 데 쓰고, 실제 계획은 더 정확한 계산으로 확인해야 합니다.

## 흔한 실수

### 실수 1. 가정 수익률을 보장 수익률처럼 본다

은행 예금 이자, 채권 수익률, 주식시장 수익률은 같은 것이 아닙니다.
어떤 rate는 미리 정해져 있고, 어떤 return은 변동하며 마이너스가 될 수도 있습니다.

계획을 쓸 때는 숫자의 성격을 분명히 표시합니다.

```text
guaranteed rate
expected return
historical average
scenario assumption
```

서로 섞으면 안 됩니다.

### 실수 2. 물가를 무시한다

물가가 오르면 미래의 balance는 오늘 같은 숫자보다 구매력이 낮을 수 있습니다.
미래의 10,000달러와 오늘의 10,000달러는 같은 힘을 갖지 않을 수 있습니다.

장기 계획에서는 가능한 한 inflation 이후의 real return도 함께 봐야 합니다.

### 실수 3. 세금과 수수료를 무시한다

수수료는 복리로 굴러갈 금액을 줄입니다.
세금은 실제로 남는 금액을 줄일 수 있습니다.
Calculator의 gross return은 after-fee, after-tax 결과보다 좋아 보일 수 있습니다.

### 실수 4. 모든 투자를 compound interest로 부른다

Compound interest는 이자가 발생하는 계좌나 부채에서 더 정확한 표현입니다.
주식 투자는 배당 재투자와 기업 성장으로 compound growth가 일어날 수 있지만, 고정 이자를 받는 구조는 아닙니다.
변동성이 있는 투자에서는 compound growth라는 표현이 더 정확할 때가 많습니다.

### 실수 5. 완벽한 금액을 기다린다

복리는 시간과 꾸준함의 영향을 크게 받습니다.
작은 습관을 일찍 시작하는 것이 더 큰 습관을 훨씬 늦게 시작하는 것보다 나을 수 있습니다.
그렇다고 모든 사람이 바로 위험자산에 투자해야 한다는 뜻은 아닙니다.
시간이라는 변수가 강력하다는 뜻입니다.

## Spreadsheet로 직접 계산하기

단순한 연간 예시는 아래 column으로 만들 수 있습니다.

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

월별 model을 만들 때는 period를 월 단위로 맞춥니다.
Annual rate와 monthly period를 섞을 때는 rate 변환을 정확히 해야 합니다.

## 실제 생활에서 활용하는 방법

복리 예시는 계획 질문에 답할 때 유용합니다.

- 매달 저축하면 얼마까지 커질 수 있는가?
- 5년 늦게 시작하면 결과가 얼마나 달라지는가?
- 수수료가 최종 금액을 얼마나 줄이는가?
- 예상보다 수익률이 낮으면 어떻게 되는가?
- 최종 금액 중 원금과 성장분의 비율은 어떻게 되는가?

가장 좋은 사용법은 비교입니다.
결정을 내리기 전에 보수적인 시나리오를 여러 개 돌려보는 것이 좋습니다.

## 함께 보면 좋은 글

- [50/30/20 예산법 쓰는 법](/ko_Economy/household-budget-50-30-20/)
- [금리와 물가가 같이 움직이는 이유](/ko_Economy/interest-rate-inflation-basics/)
- [비상금은 얼마가 적당할까](/ko_Economy/emergency-fund-how-much/)

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

개인 재무 개념을 정리하거나 가계 예산, 금리, 환율, 복리 같은 기초 판단 기준을 세울 때 참고하기 좋습니다. 이 글은 교육용이며 투자 권유가 아닙니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 기대수익률보다 현금흐름, 기간, 위험 감내도, 수수료, 세금 같은 가정을 먼저 적어야 합니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "복리 계산 예시: 돈이 돈을 버는 구조를 숫자로 이해하기" 같은 핵심 문구와 personal finance, interest rate, inflation, budget, risk 같은 기초 키워드를 조합해 보세요.

## 참고 자료

- Investor.gov, Compound Interest: https://www.investor.gov/index.php/introduction-investing/investing-basics/glossary/compound-interest
- Investor.gov, Financial Tools and Calculators: https://www.investor.gov/free-financial-planning-tools-0
- Federal Reserve Education, Simple and Compound Interest lesson: https://www.federalreserveeducation.org/teaching-resources/personal-finance/saving/simple-and-compound-interest-why-it-is-great-to-save-lesson-6b
- SEC student investing education, compound interest and Rule of 72: https://www.sec.gov/investor/students/tips.htm
