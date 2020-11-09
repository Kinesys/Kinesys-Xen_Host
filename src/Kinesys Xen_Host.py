#Kinesys Xen_Host.py
#본 소스코드는 Xen Server 7.2에서 테스트 된 코드입니다.
#!/usr/bin/env python

import XenAPI
import sys
import time

username = '' #username
password = '' #user password

def main(session):

    print">>>>>>>>>>>>>>>>>>>>>>>>>>>" + "Xen Server : ", url

    try:
        all_vms = session.xenapi.VM.get_all()

        for vm in all_vms:
            record = session.xenapi.VM.get_record(vm)

        if not record["is_control_domain"] and\

            not(record["is_a_template"]) and\

                record["power_state"] == "Running":

            for i in record["VIFs"]:
                name = record["name_label"].encode('utf-8')
                    net_ret = session.xenapi.VIF.get_record(i)['network']
                    network = session.xenapi.network.get_record(net_ret)

                    ip = session.xenapi\
                        .VM_guest_metrics.get_record(record['guest_metrics'])\
                        .get("networks", {}).get('0/ip')
                    print name, "\t", ip

            except XenAPI.Failure as e:
                print("[ERROR] : " + str(e))

                exit(1)

        if __name__ == "__main__":
            if len(sys, argv) <> 2:
                print"Usage :"
                print sys, argv[0], " <ip>"
                sys.exit(1)

            url = sys.argv[1]

            session = XenAPI.Session.('https://%s' %url)

            session.xenapi.login_with_password(username, password, "2, 3", "Example_migration_demo v1.0")

        try:
            main(session)
        finally:
            session.xenapi.session.logout()            
