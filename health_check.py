#!/usr/bin/env python3
import psutil
import socket
import emails
import os

# set system thresholds:
max_cpu_usage_perc = 80
max_disk_avail_perc = 20
max_mem_avail_mb = 500
check_local_host_ip = "127.0.0.1"


def checkCPU():
    """check if CPU usage % exceeds max threshold"""
    cpu_usage_perc = psutil.cpu_percent(interval=3)
    return cpu_usage_perc > max_cpu_usage_perc


def checkDisk():
    """check if Disk usage exceeds max threshold"""
    max_disk_usage_perc = 100 - max_disk_avail_perc
    dsk_usage_perc = psutil.disk_usage("/").percent
    return dsk_usage_perc > max_disk_usage_perc


def checkMem():
    """check if Memory usage % exceeds max threshold"""
    one_mb = 2 ** 20
    max_mem_avail = one_mb * max_mem_avail_mb
    mem_avail = psutil.virtual_memory().available
    return mem_avail < max_mem_avail


def checkNet():
    """check if local host name resolves to local IP"""
    local_host_ip = socket.gethostbyname("localhost")
    return local_host_ip != check_local_host_ip


def sendAlert(alert):
    """output alert error and send email"""
    
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = alert
    body = "Please check your system and resolve the issue as soon as possible."

    message = emails.generate_email(sender, receiver, subject, body, None)
    emails.send_email(message)
    


def main():
    # check system resources:
    print("checking system resources")
    alert = None
    if checkCPU():
        alert = f"Error - CPU usage is over {max_cpu_usage_perc}%"
    elif checkDisk():
        alert = f"Error - Available disk space is less than {max_disk_avail_perc}%"
    elif checkMem():
        alert = f"Error - Available memory is less than {max_mem_avail_mb}MB"
    elif checkNet():
        alert = f"Error - localhost cannot be resolved to {check_local_host_ip}"

    # alert if error raised:
    if alert:
        sendAlert(alert)
    else:
        print("system ok")


if __name__ == "__main__":
    main()

