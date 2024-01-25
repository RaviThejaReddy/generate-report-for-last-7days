Hi Ravi,
Please solve the following problem

Objective is to use AWS Cost Explorer API to generate a daily cost report. 

Write Python script that will eventually run in a CRON job every day at 9 AM, and computes cost report for last 7 days. Given that bill gets generated a bit late, if the report is run today, the cost will be calculated end day before yesterday.

Use 'net amortized cost', and exclude 'tax', 'credits', 'upfront cost for reservations'. 

The daily cost report will be in a table in Excel file: 
For a given tag (input, keep it configurable; example Application), show the total costs by each distinct tag value in the last 7 days. So the columns will be :  tagvalue1, tagvalue2, tagvalue3... , <notag>.  
Assume that the input tag will be a Cost Allocation Tag.  

Pls ping me if you have any questions.