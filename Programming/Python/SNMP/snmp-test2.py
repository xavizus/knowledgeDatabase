from pysnmp.hlapi import *

def walk(host, oid):
    for (errorIndication,errorStatus,errorIndex,varBinds) in nextCmd(
        SnmpEngine(),
        CommunityData('public'),
        UdpTransportTarget((host, 161)),
        ContextData(), 
        ObjectType(ObjectIdentity(oid)),
        lexicographicMode=False,
        lookupNames=True,
        lookupMib=False,
        lookupValues=True):
        if errorIndication:
            print(errorIndication, file=sys.stderr)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), 
                                file=sys.stderr)             
            break
        else:
            F=open("testFile.txt","a")
            for varBind in varBinds:
                value = varBind[0]
                print(value)
                print(varBind[1].prettyPrint())
                #F.write(' = '.join([x.prettyPrint() for x in varBind]) + "\n")

walk('router.xavizus.com','1.3.6.1.2.1.3.1.1.1')