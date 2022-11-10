#!/usr/bin/env python3

import json
import locale
import sys
import emails
import reports
import os



def main(argv):
  """Process the JSON data and generate a full report out of it."""
  summary = []
  text_files = os.listdir("/home/student-02-a90500197f9a/supplier-data/descriptions/")
  for txt in text_files: 
    with open("/home/student-02-a90500197f9a/supplier-data/descriptions/"+txt) as fileobj:
        list_of_entries = fileobj.readlines()
        summary.append("name: "+list_of_entries[0].strip())
        summary.append("weight: "+list_of_entries[1].strip())
  final_sum = ""
  count = 1
  for line in summary:
    if(count %2 !=0):
        final_sum += line+"<br/>"
    else:
        final_sum += line+"<br/><br/>"
    count += 1              
  # TODO: turn this into a PDF report
  reports.generate_report("/tmp/processed.pdf","Processed Update on March 11, 2022", final_sum)
  # TODO: send the PDF report as an email attachment
  

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send_email(message)


if __name__ == "__main__":
  main(sys.argv)
