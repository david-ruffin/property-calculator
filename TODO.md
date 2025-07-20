# Commercial Property Calculator Implementation TODO

## High Priority Tasks

### 1. Add commercial property type conditional logic to app.py
- [ ] Add `elif property_type == "Commercial":` branch after existing residential logic

### 2. Create commercial sidebar input fields
- [ ] State dropdown (H1) - default "TX"
- [ ] Purchase Price (H3) - default 1,970,000
- [ ] % Down Payment (H5) - default 30%
- [ ] **Amount Down (calculated)** - Purchase Price × % Down with color coding:
  - Green: ≤ $500,000
  - Yellow: $500,001 - $750,000  
  - Red: > $750,000
- [ ] Annual Gross Rents (K4) - default 152,195
- [ ] Annual NOI from Listing (L4) - default 106,548  
- [ ] Vacancy Rate (L5) - default 3%
- [ ] All Other Operating Expenses (J11) - default 5,000

### 3. Implement commercial loan calculation logic from Excel
- [ ] 25-year loan term (vs 30 residential)
- [ ] 6.5% interest rate (vs 2% residential)
- [ ] Commercial loan formulas

### 4. Create commercial results display
- [ ] Annual NOI Estimated calculation: `=(K4*(1-L5))-SUM(J8:J11)`
- [ ] Annual Cash Flow calculation: `=L8-L9` (NOI - Debt Service)
- [ ] Cash-on-Cash Return calculation: `=L10/L11` (Cash Flow ÷ Total Cash Down)
- [ ] Deal evaluation with color coding:
  - Green: Cash Flow > 0 (Good Deal)
  - Red: Cash Flow ≤ 0 (Bad Deal)
- [ ] Total Cash Down calculation: `=J3+H4` (Closing Costs + Down Payment)
- [ ] Closing Costs calculation: Purchase Price × 3%

## Medium Priority Tasks

### 5. Add state-based lookup tables
- [ ] Tax rates by state: AZ(0.62%), CA(1.25%), IN(1.37%), NV(0.65%), TX(1.7%), MI(3.21%)
- [ ] Insurance rates by state: All states (0.5%)
- [ ] Tax Rate Lookup: `=SUMIF(P2:P7,H1,O2:O7)`
- [ ] Insurance Rate Lookup: `=SUMIF(P2:P7,H1,Q2:Q7)`

### 6. Test commercial calculations
- [ ] Verify against Excel formulas
- [ ] Cross-check all calculations

## Notes
- Keep residential functionality unchanged
- Commercial uses different metrics than residential (NOI vs rent/occupancy)
- **ALL commercial logic sourced from Excel**: `/Users/sudo/Documents/Git/property-calculator-1/Commercial_Prop_Screening_Tool.xlsx`
- Excel cell references guide implementation (H1, H3, H5, K4, L4, L5, J11, etc.)
- State lookup tables: Tax rates (O2-O7, P2-P7) and Insurance rates (Q2-Q7)
- Commercial loan defaults: 25-year term, 6.5% interest rate
- Key Excel formulas to implement:
  - Tax Rate: `=SUMIF(P2:P7,H1,O2:O7)`
  - Amount Down: `=H3*H5`
  - Estimated NOI: `=(K4*(1-L5))-SUM(J8:J11)`
  - Cash-on-Cash Return: `=L10/L11` (Cash Flow ÷ Cash Down)