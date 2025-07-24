# Property Calculator - Project Timeline & Roadmap

## ✅ COMPLETED TASKS

### Phase 0.1: Core Commercial Implementation (Dec 2024)
- [x] Add commercial property type conditional logic to app.py *(Completed)*
- [x] Add `elif property_type == "Commercial":` branch after existing residential logic *(Completed)*

### Phase 0.2: Commercial Sidebar Input Fields (Dec 2024)
- [x] State dropdown (H1) - default "CA" (changed from "TX") *(Completed)*
- [x] Purchase Price (H3) - default 1,970,000 *(Completed)*
- [x] % Down Payment (H5) - default 30% *(Completed)*
- [x] **Amount Down (calculated)** - Purchase Price × % Down with color coding: *(Completed)*
  - Green: ≤ $500,000
  - Yellow: $500,001 - $750,000  
  - Red: > $750,000
- [x] Annual Gross Rents (K4) - default 152,195 *(Completed)*
- [x] Annual NOI from Listing (L4) - default 106,548 *(Completed)*
- [x] Vacancy Rate (L5) - default 3% *(Completed)*
- [x] All Other Operating Expenses (J11) - default 5,000 *(Completed)*

### Phase 0.3: Commercial Loan Calculations (Dec 2024)
- [x] 25-year loan term (vs 30 residential) *(Completed)*
- [x] 6.5% interest rate (vs 2% residential) *(Completed)*
- [x] Commercial loan formulas *(Completed)*
- [x] User-adjustable loan terms (1-30 years) *(Enhanced beyond original scope)*
- [x] User-adjustable interest rates *(Enhanced beyond original scope)*

### Phase 0.4: Commercial Results Display (Dec 2024)
- [x] Annual NOI Estimated calculation: `=(K4*(1-L5))-SUM(J8:J11)` *(Completed)*
- [x] Annual Cash Flow calculation: `=L8-L9` (NOI - Debt Service) *(Completed)*
- [x] Cash-on-Cash Return calculation: `=L10/L11` (Cash Flow ÷ Total Cash Down) *(Completed)*
- [x] Deal evaluation with color coding: *(Completed)*
  - Green: Cash Flow > 0 (Good Deal)
  - Red: Cash Flow ≤ 0 (Bad Deal)
- [x] Total Cash Down calculation: `=J3+H4` (Closing Costs + Down Payment) *(Completed)*
- [x] Closing Costs calculation: Purchase Price × 3% *(Completed)*

### Phase 0.5: State-Based Lookup Tables (Dec 2024)
- [x] Tax rates by state: AZ(0.62%), CA(1.25%), IN(1.37%), NV(0.65%), TX(1.7%), MI(3.21%) *(Completed)*
- [x] Insurance rates by state: AZ(0.5%), CA(1.25%), IN(0.5%), NV(0.5%), TX(0.5%), MI(0.5%) *(Completed)*
- [x] Tax Rate Lookup: `=SUMIF(P2:P7,H1,O2:O7)` *(Completed)*
- [x] Insurance Rate Lookup: `=SUMIF(P2:P7,H1,Q2:Q7)` *(Completed)*

### Phase 0.6: Testing & Validation (Dec 2024)
- [x] Verify against Excel formulas *(Completed)*
- [x] Cross-check all calculations *(Completed)*

## ✅ ADDITIONAL ENHANCEMENTS COMPLETED

### Phase 0.7: Input System Improvements (Jan 2025)
- [x] Fix sticky input behavior with callback-based updates *(Major enhancement)*
- [x] Implement `on_change` callbacks for all residential inputs *(Completed)*
- [x] Implement `on_change` callbacks for all commercial inputs *(Completed)*
- [x] Eliminate race conditions with mid-render query parameter updates *(Completed)*
- [x] Ensure instant input response without multiple clicks *(Completed)*

### Phase 0.8: URL Sharing & State Management (Jan 2025)
- [x] Add property type to query parameters *(Major enhancement)*
- [x] Property type preservation in shareable URLs *(Completed)*
- [x] Complete state preservation for all input values *(Completed)*
- [x] Cross-platform URL compatibility *(Completed)*
- [x] Bookmark-friendly calculator states *(Completed)*

### Phase 0.9: UI/UX Improvements (Jan 2025)
- [x] Move commercial state selection to Location section for consistency *(Completed)*
- [x] Add property type explanatory text: "Residential: 4 units or less | Commercial: 5 units or more" *(Completed)*
- [x] Change default state from Texas to California for both property types *(Completed)*
- [x] Enhanced tooltips and help text *(Completed)*
- [x] Color-coded visual indicators *(Completed)*

### Phase 0.10: Documentation & Project Management (Jan 2025)
- [x] Update README to reflect current application features *(Completed)*
- [x] Add Future Roadmap to README *(Completed)*
- [x] Redesign README with industry best practices and user-focused structure *(Completed)*
- [x] Transform technical documentation into compelling user experience *(Completed)*

## 🚧 NEXT UP - PHASE 1: Property URL Integration

### 1.1: Property URL Input Fields
- [ ] Add property URL input field for residential properties in sidebar
- [ ] Add property URL input field for commercial properties in sidebar
- [ ] Add button next to each URL field (button text TBD - maybe "View Property" or "Open Listing")
- [ ] Button opens the URL in a new tab when clicked

### 1.2: URL Storage & Query Parameters
- [ ] Include property URLs in query parameters so they're preserved in shareable calculator URLs
- [ ] Add property URL to query parameters for residential (`property_url`)
- [ ] Add property URL to query parameters for commercial (`comm_property_url`)
- [ ] Implement callback-based updates for URL fields

### 1.3: Test Complete Sharing Experience
- [ ] Test that shared links include both calculator settings AND property URLs
- [ ] Verify recipient gets complete context: calculations + direct access to property listing
- [ ] Ensure investment team can share analysis back and forth with full context intact

## 🔮 FUTURE - PHASE 2: Auto-Population from URLs

### 2.1: Auto-Population Button & Logic
- [ ] Add second button next to URL fields (maybe "Get Information" or "Import Data")
- [ ] Auto-populate **only the sidebar input fields** from listing URL in real-time
- [ ] Extract data via MCP, N8N, or similar integration

### 2.2: Data Extraction Scope (Sidebar Fields Only)
**Residential:**
- [ ] Purchase Price
- [ ] Down Payment % (if available)
- [ ] Expected Monthly Rent
- [ ] State/Location

**Commercial:**
- [ ] Purchase Price  
- [ ] Down Payment % (if available)
- [ ] Annual Gross Rents
- [ ] Annual NOI (if available)
- [ ] State/Location

### 2.3: Platform Integration
- [ ] LoopNet listing data extraction
- [ ] Zillow property data extraction
- [ ] Other major listing platforms (Crexi, etc.)

**Note:** Tax rates, insurance rates, and all calculated fields remain hard-coded in the app. Only extract user-input fields from the left sidebar.

## 📋 PROJECT NOTES & TECHNICAL DETAILS

### Implementation Guidelines
- **Residential functionality**: Keep unchanged and fully preserved
- **Commercial calculations**: Different metrics than residential (NOI vs rent/occupancy)
- **Excel source validation**: ALL commercial logic sourced from `Commercial_Prop_Screening_Tool.xlsx`
- **State consistency**: Both property types default to California
- **Input system**: Callback-based updates prevent sticky behavior

### Excel Formula References (Completed Implementation)
- Tax Rate Lookup: `=SUMIF(P2:P7,H1,O2:O7)` ✅
- Amount Down Calculation: `=H3*H5` ✅  
- NOI Estimation: `=(K4*(1-L5))-SUM(J8:J11)` ✅
- Cash-on-Cash Return: `=L10/L11` (Cash Flow ÷ Cash Down) ✅

### State Data Tables (Implemented)
- **Tax Rates**: AZ(0.62%), CA(1.25%), IN(1.37%), NV(0.65%), TX(1.7%), MI(3.21%) ✅
- **Insurance Rates**: AZ(0.5%), CA(1.25%), IN(0.5%), NV(0.5%), TX(0.5%), MI(0.5%) ✅

### Context Continuity Notes
- **Current Status**: Full-featured calculator with URL sharing, responsive inputs, and professional documentation
- **Architecture**: Streamlit + callback-based inputs + query parameter state management  
- **Next Milestone**: Property URL integration (Phase 1) to enable investment team collaboration
- **Use Case**: Investment team shares calculator links with property context - analyze → share → collaborate → decide
- **Long-term Vision**: Auto-populate sidebar fields from listing URLs (Phase 2) for faster property evaluation