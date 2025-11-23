# Ghana-mobile-money-insights

An end-to-end data engineering and analytics project focused on Mobile Money (MoMo) usage trends in Ghana. The project starts from a raw transactional dataset and performs exploratory data analysis (EDA) to reveal patterns in financial behaviour across regions, age groups, gender and time.

---

## 1. Project Overview

**Goal:**

- Understand how Ghanaians use Mobile Money across regions and demographics.
- Simulate a realistic Ghana-style MoMo dataset and use it to generate insights that could inform policy, product design and financial inclusion strategies.

**Key Questions:**

- How is transaction activity distributed across regions in Ghana?
- Which age groups are most active on Mobile Money?
- Are there noticeable differences between male and female usage?
- At what times of day do people transact the most?
- How are transaction amounts distributed (small vs. large values)?

The project is organised into:

- `notebooks/analysis.ipynb` – data cleaning and enrichment.
- `notebooks/eda.ipynb` – exploratory data analysis and visualisations.
- `data/` – raw and cleaned datasets (large CSVs are **not** stored in GitHub; see Data Access note below).

---

## 2. Data and Preparation

The dataset contains individual Mobile Money transactions with the following key fields:

- Transaction amount
- Timestamp (date and hour of the transaction)
- Customer region (16 administrative regions of Ghana)
- Customer age group (18–24, 25–34, 35–44, 45–54, 55–64, 65+)
- Customer gender (male/female)

Before analysis, the data is checked and cleaned:

- Duplicate records are removed.
- Rows with missing key fields (amount, timestamp, region, age, gender) are dropped.
- Technical index columns that do not carry business meaning are excluded.

After cleaning:

- There are no missing values in the analytical dataset.
- The remaining columns are consistent and ready for descriptive and visual analysis.

This ensures that the patterns observed in the analysis are not driven by data quality issues such as nulls or duplicates.

---

## 3. Transaction Volumes and Amounts

### 3.1 Volume overview

- The dataset contains a large number of transactions, confirming that MoMo is used at scale across the country.
- Basic descriptive statistics show a wide range of transaction values, from very small everyday transfers to much larger payments.

### 3.2 Amount distribution

- The distribution of transaction amounts is **right-skewed**:
  - The majority of transactions are small to medium in size, consistent with:
    - Airtime/data top-ups
    - Person-to-person (P2P) transfers
    - Utility bill payments
    - Merchant payments for everyday purchases
  - A smaller number of high-value transactions represents:
    - Business payments
    - Rent and school fees
    - Bulk transfers and remittances

- Boxplots and histograms confirm:
  - A dense cluster of low-to-mid-value transactions.
  - A noticeable tail of high-value transactions and some outliers.

From a business perspective, this means MoMo must support both high-frequency micro-payments and lower-frequency but higher-value transactions, each with appropriate risk controls and user experience.

---

## 4. Regional Insights

### 4.1 Transaction distribution by region

When counting transactions by region, clear patterns emerge:

- **Greater Accra** and **Ashanti** account for the highest volumes of MoMo activity.
  - This aligns with their roles as Ghana’s most populous and economically active regions.
  - Dense agent networks, higher smartphone penetration, and more formal employment likely contribute to this dominance.
- **Eastern, Central and Western** regions also contribute substantial transaction volumes.
  - These regions show strong linkages to trade, commuting, and regional commerce.
- Northern and newer regions (such as Savannah, North East, Oti, Western North) record lower but meaningful levels of activity.
  - This suggests that while MoMo has reached these areas, there is still room for growth in access, usage depth, and agent coverage.

### 4.2 Implications

- Urban and peri-urban centres are currently the engine of MoMo transaction volume.
- Expansion strategies (agent deployment, marketing, merchant acquisition) can prioritise:
  - Strengthening already strong regions to sustain revenue.
  - Targeted growth in under-served regions to improve financial inclusion.

---

## 5. Demographic Insights

### 5.1 Age groups

Analysing transaction counts by age group reveals:

- **18–24 and 25–34** are the most active MoMo users by volume.
  - These groups are digitally savvy, mobile-first, and use MoMo as a primary financial tool.
- The **35–44** age group also contributes significantly, especially in larger transaction values.
- Usage gradually declines in:
  - **45–54**
  - **55–64**
  - **65+**

In terms of amounts:

- Younger users (18–24, 25–34) tend to perform many lower-value transactions:
  - Airtime, small P2P transfers, small merchant payments.
- Mid-age groups (35–44, 45–54) are more prominent in larger-value transactions:
  - Business payments, rent, fees, family support.

### 5.2 Gender

The dataset shows a slight **male majority** in transaction counts:

- Men perform more transactions on average than women.
- When comparing average amounts:
  - Male-led transactions can trend slightly higher in value in some segments.
  - However, women still represent a significant share of both volume and value.

This pattern is consistent with broader financial inclusion trends where:

- Men are often earlier adopters of digital financial tools.
- Women may face more barriers (documentation, phone access, income levels, cultural norms).

### 5.3 Implications

- There is a real opportunity to **close the gender gap**:
  - Design products and campaigns specifically for women (e.g., savings groups, micro-insurance, micro-loans).
  - Work with female-dominated sectors (markets, trade, agriculture) to increase merchant MoMo acceptance.
  - Provide targeted financial literacy and digital skills training.

---

## 6. Time-of-Day and Daily Patterns

By examining the hour of each transaction, a clear daily usage cycle appears:

- **00:00–05:00 (Late night / early morning)**
  - Very low activity, as expected when most users are asleep.
- **06:00–09:00 (Morning)**
  - Gradual increase in transactions as people start their day:
    - Transport and commuting-related payments.
    - Early airtime/data top-ups.
- **10:00–16:00 (Core business hours)**
  - Peak transaction window:
    - Salary disbursements.
    - Business and merchant payments.
    - Bill settlements and bulk transfers.
- **17:00–21:00 (Evening)**
  - Secondary peak:
    - People send family support, pay for utilities, or make end-of-day purchases.
- **After 21:00**
  - Activity declines sharply as households wind down.

### 6.1 Operational implications

- System performance, uptime, and agent liquidity must be strongest between late morning and evening peaks.
- Planned maintenance should avoid these peak hours to minimise user disruption.

---

## 7. Synthesis and Recommendations

Bringing the regional, demographic, and temporal findings together:

1. **Focus on high-activity regions while nurturing emerging ones**
	- Maintain strong infrastructure and user experience in Greater Accra and Ashanti.
	- Identify growth opportunities in mid-tier regions (Eastern, Central, Western).
	- Invest in awareness, agent networks, and merchant acceptance in under-served northern and newly created regions.

2. **Build products for the core user base (18–44)**
	- Young and working-age adults drive MoMo volumes and, in many cases, value.
	- Tailor offerings around:
	  - Everyday payments (transport, airtime, utilities).
	  - Small business needs (inventory purchases, customer collections).
	  - Savings and credit tools that are simple and mobile-first.

3. **Address the gender gap with targeted interventions**
	- Understand barriers faced by women in adopting and using MoMo.
	- Partner with organisations and communities to:
	  - Provide digital and financial education.
	  - Promote women-led merchants.
	  - Design use cases that are directly relevant to women’s economic activities.

4. **Align operations with usage peaks**
	- Ensure system reliability and liquidity during 10:00–16:00 and 17:00–21:00.
	- Use transaction pattern data to plan:
	  - Cash management for agents.
	  - Customer support staffing.
	  - Scheduled maintenance windows.

5. **Support both micro and high-value transactions**
	- Maintain low-friction experiences for small, frequent payments.
	- Strengthen security, limits, and authentication for larger-value transactions.
	- Consider differentiated pricing or loyalty schemes to balance volume and value.

---

## 8. How to Reproduce the Analysis

### 5.1 Setup

1. Create and activate a virtual environment (optional but recommended):

	```powershell
	python -m venv venv
	venv\Scripts\activate
	```

2. Install dependencies:

	```powershell
	pip install -r Requirements.txt
	```

### 5.2 Data access

- The raw and cleaned CSV files are large and are **not stored in this GitHub repository** to avoid size limits.
- To run the notebooks end-to-end:
  - Obtain `data/mobile_money_transactions.csv` (raw) and/or `data/mobile_money_transactions_cleaned.csv` (cleaned) from the project owner (e.g., shared via Telegram or cloud storage).
  - Place the files under the `data/` folder:

	 ```text
	 data/mobile_money_transactions.csv
	 data/mobile_money_transactions_cleaned.csv
	 ```

### 5.3 Run the notebooks

1. Open `notebooks/analysis.ipynb` and run all cells to:
	- Clean the raw dataset.
	- Add gender, region, age group and timestamp.
	- Introduce realistic variation and save the cleaned CSV.

2. Open `notebooks/eda.ipynb` and run all cells to:
	- Inspect data quality.
	- Plot transaction amount distributions.
	- Analyse activity by region, age group, gender and time-of-day.
	- View correlation heatmaps and other summary visuals.

---

## 6. Future Work

Potential extensions of this project include:

- Building a **dashboard** (e.g., in Power BI, Tableau or Plotly Dash) for interactive exploration of MoMo behaviour.
- Adding **predictive models**, such as churn prediction, fraud detection or credit scoring based on transaction histories.
- Incorporating **official statistics** from Ghana Statistical Service, Bank of Ghana, NCA or GSMA to further calibrate the synthetic distributions.
- Packaging the cleaning and EDA logic as a **reusable Python module** or data engineering pipeline (e.g., Airflow, Prefect).

This README serves as a high-level narrative report of the analysis and a starting point for deeper exploration.
