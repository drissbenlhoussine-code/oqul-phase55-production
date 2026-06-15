# Guide 03: Invoice Template & Pricing Calculator
## How to Invoice Professionally and Price Your Products/Services

---

## Overview

Two of the biggest mistakes small business owners make are undercharging for their work and invoicing unprofessionally. These two issues are more connected than they might seem — when you lack confidence in your pricing, it often shows up in hesitant, informal invoicing practices. When your invoicing is inconsistent or unclear, clients delay payment, misunderstand terms, and lose confidence in your professionalism. The Invoice Template and Pricing Calculator in this toolkit are designed to solve both problems simultaneously: the Pricing Calculator gives you the clarity and confidence to charge what you're truly worth, and the Invoice Template gives you the professional presentation to collect that payment efficiently and without friction.

---

## Part 1: Invoice Template (05_Invoice_Template.html)

### What It Is

The Invoice Template is a professionally formatted HTML file that you can open in any web browser, customize with your business and client details, and print or save as a PDF to send to clients. It includes all the standard components of a professional invoice: your business information, client details, an itemized list of services or products, subtotal, tax (if applicable), total due, payment terms, and payment instructions. Using a consistent, branded invoice template sends a clear signal to clients that you are an organized, professional business — and that you expect to be paid on time and in full.

### How to Customize Your Invoice Template

1. **Open the file in a text editor** (such as Notepad, TextEdit, VS Code, or Sublime Text) to edit the content. Do not edit it in a web browser — browsers display the rendered result, not the editable code.
2. **Replace the placeholder business information** at the top of the template with your real business name, address, phone number, email address, and website. If you have a business logo, you can add it by replacing the logo placeholder with an `<img>` tag pointing to your logo file.
3. **Update the invoice number system.** Use a consistent numbering format such as INV-2024-001, INV-2024-002, etc. A sequential numbering system makes it easy to reference invoices in conversation and to track them in your records.
4. **Customize the payment terms section.** Your payment terms should clearly state: how many days the client has to pay (Net 7, Net 14, Net 30), accepted payment methods, and any late payment penalties.
5. **Add or remove line items** in the itemized services table to match the work you completed. Each line item should include a description, quantity, unit price, and line total.
6. **Update the tax section** if you are required to charge sales tax, GST, VAT, or any other applicable tax. If you are not required to charge tax, remove this section entirely to avoid confusion.
7. **Add your payment instructions.** Include your bank account details (for bank transfer), PayPal email address, or a payment link (such as a Stripe payment link or PayPal.me URL) so clients know exactly how to pay.

### Understanding Each Field

- **Invoice Number:** A unique identifier for this invoice. Essential for reference in communications and for matching payments to invoices in your Income Tracker.
- **Invoice Date:** The date you issue the invoice. This is the starting point for your payment terms countdown.
- **Due Date:** The date by which payment must be received. Calculate this from the Invoice Date based on your payment terms (e.g., if invoice date is January 1 and terms are Net 14, due date is January 15).
- **Bill To:** Your client's name, business name, and mailing or billing address. Some clients require their company address on invoices for accounting purposes — ask if you're unsure.
- **Itemized Services/Products:** A line-by-line breakdown of everything you're charging for. Be specific and descriptive — "Brand Identity Design Package — Logo, Color Palette, Typography Guide, Brand Guidelines PDF" is far more professional than "Design Work."
- **Subtotal:** The total before tax.
- **Tax:** Only include if you are legally required to collect and remit tax. Include your tax registration number if applicable.
- **Total Due:** The final amount the client owes.
- **Payment Terms:** The rules governing how and when payment is expected.
- **Notes:** Any additional context — a thank-you message, project reference number, or reminder of what's included.

### How to Save Your Invoice as a PDF

1. **Open the customized HTML file in Google Chrome** (or any modern web browser).
2. **Press Ctrl+P (Windows) or Cmd+P (Mac)** to open the print dialog.
3. **Change the destination to "Save as PDF"** in the print dialog.
4. **Adjust the layout to Portrait** and set margins to "Default" or "Minimum."
5. **Click Save** and choose a clear file name such as: `INV-2024-001_ClientName.pdf`
6. **Send the PDF to your client** via email. Never send the raw HTML file — always convert to PDF first to ensure consistent formatting on the client's end.

### Professional Invoicing Tips

- **Invoice immediately upon project completion.** The sooner you invoice, the sooner you get paid. Delaying invoicing is one of the leading causes of cash flow problems in small businesses.
- **Require a deposit before starting work.** For projects over a certain value (define your threshold), require 30–50% upfront before you begin. This protects your time and filters out less serious clients.
- **Follow up on overdue invoices without hesitation.** Send a friendly reminder at 1 day past due, a firm reminder at 7 days past due, and a formal notice at 14 days past due. Most late payments are due to oversight, not intentional non-payment — prompt follow-up resolves them quickly.
- **Specify late payment fees in your terms.** A standard late payment fee is 1.5% per month on overdue balances. Even if you never enforce it, having it in writing sets a professional tone and motivates timely payment.
- **Keep a copy of every invoice you send.** Maintain a folder (Google Drive, Dropbox, or local) organized by year and client, containing the PDF of every invoice issued. This is essential for your records and for tax purposes.

### What to Include in Payment Terms

Your payment terms section should clearly answer four questions for the client:

1. **When is payment due?** (e.g., "Payment due within 14 days of invoice date.")
2. **How can payment be made?** (e.g., "Accepted payment methods: bank transfer, PayPal, Stripe. Payment details below.")
3. **What happens if payment is late?** (e.g., "A late payment fee of 1.5% per month will be applied to balances unpaid after the due date.")
4. **What is the refund/revision policy?** (e.g., "Deposits are non-refundable. Revisions beyond the agreed scope will be quoted separately.")

Well-written payment terms prevent the vast majority of payment disputes and misunderstandings before they happen.

---

## Part 2: Pricing Calculator (07_Pricing_Calculator.csv)

### What It Is

The Pricing Calculator helps you determine the right price for your products or services based on a complete picture of your true costs — not just the obvious ones. Many small business owners underprice their work because they account for materials but forget to factor in their time, their overhead costs, platform fees, and a sustainable profit margin. The result is a price that feels competitive but actually leaves money on the table or, worse, results in working for less than minimum wage once all costs are considered. The Pricing Calculator changes that by walking you through every cost component and helping you calculate a price that is both fair to clients and sustainable for your business.

### Understanding Your True Costs

Before you can price profitably, you need to understand all of the costs involved in delivering your product or service. There are three main cost categories:

**1. Direct Costs (also called Cost of Goods Sold or COGS)**
These are costs directly tied to producing a specific product or delivering a specific service:
- Raw materials or supplies
- Packaging and shipping supplies (for physical products)
- Freelancer or contractor costs (if you outsource any part of delivery)
- Platform or marketplace fees (Etsy fees, Shopify transaction fees, etc.)
- Payment processing fees

**2. Labor Costs (Your Time)**
This is the cost of your own time — and it is the most commonly undervalued or completely forgotten cost for self-employed business owners. To calculate your hourly labor cost:
- Determine how much you want (or need) to earn per year
- Divide by the number of billable hours you can realistically work per year (most service providers have 800–1,200 truly billable hours per year after accounting for admin, marketing, and business development time)
- The result is your minimum required hourly rate before profit

**3. Overhead Costs**
These are the ongoing business costs not tied to any single project or product:
- Software subscriptions (design tools, accounting software, email marketing, etc.)
- Website hosting and domain fees
- Professional development and education
- Marketing and advertising costs
- Office supplies
- A portion of phone and internet bills used for business

To allocate overhead to individual products or services, total your monthly overhead costs, estimate how many units you sell or projects you complete per month, and divide overhead by that number to get a per-unit overhead allocation.

### Calculating Labor Correctly

The most critical — and most misunderstood — component of pricing for service providers is the true cost of your labor. Here is a step-by-step approach:

1. **Determine your desired annual income.** This is what you want to actually take home after taxes and business expenses — not just gross revenue.
2. **Add your estimated annual tax liability.** Self-employed individuals typically pay 25–35% in combined income and self-employment taxes, depending on jurisdiction. Add this to your desired take-home income.
3. **Add your estimated annual business expenses (overhead).** This is your annual overhead total.
4. **Total the above three figures.** This is your required annual gross revenue.
5. **Estimate your annual billable hours.** Be realistic — most self-employed service providers can bill for 15–25 hours per week when accounting for all non-billable time.
6. **Divide required annual gross revenue by annual billable hours.** The result is your minimum hourly rate.

**Example:** You want $60,000 take-home pay. You estimate $20,000 in taxes and $10,000 in overhead. Total required revenue = $90,000. You estimate 1,000 billable hours per year. Minimum hourly rate = $90,000 ÷ 1,000 = **$90/hour.**

### Choosing the Right Profit Margin

Once you've calculated your break-even price (the price that covers all costs with no profit), you need to add your profit margin. Profit is not greed — it is what funds business growth, builds reserves for slow seasons, and compensates you for the risk of running your own business.

Recommended margin ranges by business type:

- **Service businesses (design, writing, coaching, consulting):** 30–60% profit margin above full cost
- **Physical product businesses (handmade goods, retail):** 40–70% above COGS
- **Digital products (printables, templates, courses):** 60–90% above production cost (since marginal cost per additional unit is near zero)
- **Wholesale pricing:** Typically 50% of retail price (keystone pricing) or your cost × 2

**Margin Formula:** Price = Total Cost ÷ (1 − Desired Margin %)

Example: If your total cost per unit is $12 and you want a 60% margin: Price = $12 ÷ (1 − 0.60) = $12 ÷ 0.40 = **$30.00**

### Pricing Psychology Tips

Pricing is not only a math problem — it is also a perception problem. How you present your price matters as much as the number itself.

- **Anchor with a higher option.** When presenting multiple service packages, always lead with your premium option. This makes your middle-tier option feel like a reasonable compromise rather than an expensive choice.
- **Avoid round numbers for premium services.** $97 feels more considered and specific than $100. $1,497 feels more researched than $1,500. Use this sparingly and intentionally.
- **Price by value, not by time.** For service businesses, pricing by deliverable or by outcome — rather than by the hour — allows you to capture the full value of your expertise and efficiency. A client doesn't pay less because you've gotten faster through experience; they pay for the result.
- **Bundle strategically.** Bundling services or products together at a modest discount increases average transaction value and makes comparison shopping harder. A "Starter Package," "Growth Package," and "Premium Package" gives clients clear choices without triggering price shopping.
- **Be confident in your prices.** Hesitating, apologizing, or immediately offering discounts when a client asks about price signals that you don't fully believe in your own value. State your price clearly and let the silence sit.

### Competitive Pricing Considerations

Understanding where your prices sit relative to competitors is useful context — but it should not be the primary driver of your pricing decisions. Here's how to use competitive research intelligently:

1. **Research competitor pricing as a sanity check**, not as a ceiling. If all competitors charge $50–$80 for a similar service and your cost-based calculation produces $120, investigate why — but don't automatically lower your price. Your costs, quality, or niche positioning may genuinely justify a higher rate.
2. **Identify the tier you want to occupy.** Are you the affordable option, the mid-market choice, or the premium provider? Each tier requires a different value proposition. You can be highly profitable in any tier if your positioning is clear and consistent.
3. **Never compete purely on price.** If your only differentiator is being the cheapest option, you will always be vulnerable to someone cheaper coming along. Compete on quality, specialization, turnaround time, customer experience, or a unique niche.
4. **Raise your prices as your experience grows.** Your rates should increase at least annually to reflect your growing expertise, reputation, and the increased value you deliver. A modest 10–15% annual rate increase is standard practice for service providers.
5. **Test price increases on new clients first.** If you're unsure whether the market will accept a higher rate, test it on new inquiries before changing rates for existing clients. Track your conversion rate — if it holds steady or improves, your new price is working.

---

## Pricing Strategy Advice

### For Service Businesses

The most common pricing mistake for service providers is pricing based on what competitors charge without doing the underlying cost math. Start with your required hourly rate (calculated above), build packages around common client needs, price each package by estimated hours × hourly rate + overhead allocation + profit margin, and then validate against the market. If your prices are significantly above market, look for ways to reduce overhead or reframe your value proposition rather than automatically reducing your rate.

### For Product-Based Businesses

Physical product pricing must account for COGS, packaging, shipping materials, platform fees, and your time for production and fulfillment. A common mistake is pricing on COGS alone and forgetting time. If it takes you 30 minutes to make a candle and you want to earn $40/hour for your labor, that candle has a $20 labor cost before you add materials. Price accordingly.

### For Digital Product Sellers

Digital products have the unique advantage of near-zero marginal cost — once the product is created, each additional sale is almost pure profit. This means you can afford to price strategically based on perceived value rather than production cost. Research what your target audience is willing to pay, look at competitor pricing on platforms like Etsy, and test different price points. Many digital product sellers find that modest price increases (from $4.99 to $6.99, for example) have no negative impact on sales volume but significantly improve revenue and profit margin.

### Reviewing and Adjusting Your Pricing

Commit to reviewing your pricing on a defined schedule — at minimum, annually, and ideally every 6 months. At each review:
- Has your cost structure changed? (New software, increased materials costs, higher platform fees?)
- Has your skill level, reputation, or portfolio grown?
- Are you consistently booked out or frequently turning away work? (This is a clear signal to raise prices.)
- Are your profit margins healthy enough to sustain and grow your business?

Pricing is not a set-and-forget decision. It is a dynamic, ongoing aspect of your business strategy that rewards regular attention and adjustment.

---

## Important Disclaimer

The invoicing template, pricing calculator, and guidance provided in this guide are for informational and organizational purposes only. They do not constitute professional financial, legal, accounting, or tax advice. Tax obligations related to invoicing (such as when and how to charge sales tax, VAT, or GST), contract and payment term enforceability, and appropriate pricing strategies vary significantly by jurisdiction, business structure, and industry. Please consult a qualified accountant, business attorney, or financial advisor before finalizing your invoicing practices, payment terms, or pricing structure, particularly if you operate across multiple states or countries.
