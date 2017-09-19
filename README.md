#README#

## Pre-Requisites: ##

     * Exports of specific Mailchimp account campaigns(if you need to know, you'll know)

     * Create a folder named 'chimpify' in your Documents directory

     * A 'testYESFAC' and a 'testNOFAC' folder should be created within the newly created 'chimpify' directory


## Uses: ##

        This program is used for manipulating data within multiple .csv files that have	been exported from a specific mailchimp

        account campaign with the intent of uploading a single unified csv into a datatable.

	   To get gritty, mailchimp does not allow you to export a full list from a campaign that would contain all of the fields

        you would receive when exporting individually based on subscriber type. For instance, the 'unsubscribes' subtype returns
  
        columns with why they unsubscribed, or the 'bounced' subtype returns columns with what type of bounce occurred.

        Additionally, exporting individually allows me to notate opens and clicks by a column, however this raises issues with

        duplicates which needs to be solved efficiently and with care. So I created this automation.


## How to operate: ##

1. run chimpify_NOFACS_00028.py to manipulate No Facilities data or run chimpify_YESFACS_00028.py to manipulate Yes Facilities data
 
2. Click "Select a File"

3. Select "Open the CLICKS .csv" and choose the mailchimp-clicks.csv to add the appropriate missing columns and print out a new       .csv with the appropriate columns

4. Select "Open the OPENED .csv" and choose the mailchimp-opened.csv to add the appropriate missing columns and print out a new .csv

5. Select "Concat opens and clicks", you will be prompted to select two .csv files. Select the new Opens.csv file created by the "Open the OPENED" command first, then select the new Clicks.csv file created by the "Open the CLICKS" command. This will combine both .csv's into a new .csv. The order you choose the files does not matter. 

6. Select "Dedupe opens and clicks", select the new concat.csv file created by the "Concat opens and clicks" command. This removes duplicates from the concatenated file preserving click column information.

7. Select "Open the NOT-OPENED" and choose the mailchimp-notopened.csv to add the appropriate missing columns and print out a new .csv with the appropriate columns.

8. Select "Open the BOUNCES" and choose the mailchimp-bounces.csv to add the appropriate missing columns and print out a new .csv with the appropriate columns.

9. Select "Open the UNSUBS" and choose the mailchimp-unsubs.csv to add the appropriate missing columns and print out a new .csv with the appropriate columns.

10. Select "concat all files" and choose the newly created dedupe.csv, notopened.csv, bounces.csv, and unsubs.csv in file selection. Click Open. This will add all files into one unified .csv.

11. Select "Finalize" and choose the newly created concatall.csv This will remove duplicates preserving integrity of clicks, opens, and unsubs first.

12. Revel in the hours of your time saved!# Chimpify
# Chimpify
# Chimpify
