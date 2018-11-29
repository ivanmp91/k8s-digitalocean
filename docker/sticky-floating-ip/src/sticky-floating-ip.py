#!/usr/bin/env python3
import digitalocean
import argparse
import os
from time import sleep

def main():
    secret_token=os.environ['DO_SECRET_TOKEN']
    parser = argparse.ArgumentParser(description='Digital Ocean auto assign floating ip to k8s worker droplet')
    parser.add_argument('--tag','-t' , type=str,
                    help='droplet tag where floating ip is assigned')
    parser.add_argument('--ip','-i', type=str,
                    help='Floating IP to assign')
    args = parser.parse_args()
    assign_floating_ip(args.tag,args.ip,secret_token)

def assign_floating_ip(droplet_tag,floating_ip,secret_token):
    k8s_worker_tag="k8s"
    sleep_time=10
    while 1:
        manager=digitalocean.Manager(token=secret_token)
        k8s_worker_node=manager.get_all_droplets(tag_name=k8s_worker_tag)
        k8s_droplet=k8s_worker_node.pop()
        try:
            droplet_tags=k8s_droplet.tags
            assigned_tag=False
            for tag in droplet_tags:
                if tag == droplet_tag:
                    assigned_tag=True
            if not assigned_tag:
                floating_ip=manager.get_floating_ip(ip=floating_ip)
                floating_ip.assign(k8s_droplet.id)
                tag_droplet(droplet_tag,k8s_droplet.id,secret_token)
        except digitalocean.DataReadError as e:
            print(e)
        sleep(sleep_time)

def tag_droplet(droplet_tag,droplet_id,secret_token):
    droplet_tag=digitalocean.Tag(token=secret_token, name=droplet_tag)
    droplet_tag.create()
    droplet_tag.add_droplets(droplet_id)

if __name__ == "__main__":
    main()
