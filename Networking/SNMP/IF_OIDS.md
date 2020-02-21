IF MIB are for network interfaces and status and statistics.
The highest point of IF OID are: 1.3.6.1.2.1.2

Following Object names that are somewhat interesting:
- ifInOctets (interface inbound traffic in bytes) Notice: if you got highspeed network, this value may rollback to 0 in just 40 seconds to 5 minutes.
- ifHCInOctets (interface inbound in bytes)
- ifOutOctets (interface outbound traffic in bytes) Notice: if you got highspeed network, this value may rollback to 0 in just 40 seconds to 5 minutes.
- ifHCOutOctets(interface outbound traffic in bytes)
- ifAlias (Get description/alias fro the interface)
- ifOperStatus (Gets operation status, 1 up, 2 down, 3 testing, 4 unknonw, 5 dormant, 6 notPresent, 7 lowerLayerDown)

Other intrensting OIDS that doesn't have a object name:
1.3.6.1.2.1.3.1.1 - Is an entry point for each Network address bound to which physical port, IP-address and Mac-address.
Example: 
1.3.6.1.2.1.3.1.1.1.4.1.192.168.2.3 = 4 #The 4 last digits are the ip-Address, and it is existent behind port 4.
1.3.6.1.2.1.3.1.1.2.4.1.192.168.2.3 = 0x14dae9152151 # The Ip-address got the following mac-address. Extract 0x to get mac-address.

|Object-Name|Object|Identifier|
|---|---|---|
interfaces|interfaces|1.3.6.1.2.1.2
ifNumber|ifNumber|1.3.6.1.2.1.2.1
ifTable|ifTable|1.3.6.1.2.1.2.2
ifEntry|ifEntry|1.3.6.1.2.1.2.2.1
ifIndex|ifIndex|1.3.6.1.2.1.2.2.1.1
ifInOctets|ifInOctets|1.3.6.1.2.1.2.2.1.10
ifInUcastPkts|ifInUcastPkts|1.3.6.1.2.1.2.2.1.11
ifInNUcastPkts|ifInNUcastPkts|1.3.6.1.2.1.2.2.1.12
ifInDiscards|ifInDiscards|1.3.6.1.2.1.2.2.1.13
ifInErrors|ifInErrors|1.3.6.1.2.1.2.2.1.14
ifInUnknownProtos|ifInUnknownProtos|1.3.6.1.2.1.2.2.1.15
ifOutOctets|ifOutOctets|1.3.6.1.2.1.2.2.1.16
ifOutUcastPkts|ifOutUcastPkts|1.3.6.1.2.1.2.2.1.17
ifOutNUcastPkts|ifOutNUcastPkts|1.3.6.1.2.1.2.2.1.18
ifOutDiscards|ifOutDiscards|1.3.6.1.2.1.2.2.1.19
ifDescr|ifDescr|1.3.6.1.2.1.2.2.1.2
ifOutErrors|ifOutErrors|1.3.6.1.2.1.2.2.1.20
ifOutQLen|ifOutQLen|1.3.6.1.2.1.2.2.1.21
ifSpecific|ifSpecific|1.3.6.1.2.1.2.2.1.22
ifType|ifType|1.3.6.1.2.1.2.2.1.3
ifMtu|ifMtu|1.3.6.1.2.1.2.2.1.4
ifSpeed|ifSpeed|1.3.6.1.2.1.2.2.1.5
ifPhysAddress|ifPhysAddress|1.3.6.1.2.1.2.2.1.6
ifAdminStatus|ifAdminStatus|1.3.6.1.2.1.2.2.1.7
ifOperStatus|ifOperStatus|1.3.6.1.2.1.2.2.1.8
ifLastChange|ifLastChange|1.3.6.1.2.1.2.2.1.9
ifMIB|ifMIB|1.3.6.1.2.1.31
ifMIBObjects|ifMIBObjects|1.3.6.1.2.1.31.1
ifXTable|ifXTable|1.3.6.1.2.1.31.1.1
ifXEntry|ifXEntry|1.3.6.1.2.1.31.1.1.1
ifName|ifName|1.3.6.1.2.1.31.1.1.1.1
ifHCOutOctets|ifHCOutOctets|1.3.6.1.2.1.31.1.1.1.10
ifHCOutUcastPkts|ifHCOutUcastPkts|1.3.6.1.2.1.31.1.1.1.11
ifHCOutMulticastPkts|ifHCOutMulticastPkts|1.3.6.1.2.1.31.1.1.1.12
ifHCOutBroadcastPkts|ifHCOutBroadcastPkts|1.3.6.1.2.1.31.1.1.1.13
ifLinkUpDownTrapEnable|ifLinkUpDownTrapEnable|1.3.6.1.2.1.31.1.1.1.14
ifHighSpeed|ifHighSpeed|1.3.6.1.2.1.31.1.1.1.15
ifPromiscuousMode|ifPromiscuousMode|1.3.6.1.2.1.31.1.1.1.16
ifConnectorPresent|ifConnectorPresent|1.3.6.1.2.1.31.1.1.1.17
ifAlias|ifAlias|1.3.6.1.2.1.31.1.1.1.18
ifCounterDiscontinuityTime|ifCounterDiscontinuityTime|1.3.6.1.2.1.31.1.1.1.19
ifInMulticastPkts|ifInMulticastPkts|1.3.6.1.2.1.31.1.1.1.2
ifInBroadcastPkts|ifInBroadcastPkts|1.3.6.1.2.1.31.1.1.1.3
ifOutMulticastPkts|ifOutMulticastPkts|1.3.6.1.2.1.31.1.1.1.4
ifOutBroadcastPkts|ifOutBroadcastPkts|1.3.6.1.2.1.31.1.1.1.5
ifHCInOctets|ifHCInOctets|1.3.6.1.2.1.31.1.1.1.6
ifHCInUcastPkts|ifHCInUcastPkts|1.3.6.1.2.1.31.1.1.1.7
ifHCInMulticastPkts|ifHCInMulticastPkts|1.3.6.1.2.1.31.1.1.1.8
ifHCInBroadcastPkts|ifHCInBroadcastPkts|1.3.6.1.2.1.31.1.1.1.9
ifStackTable|ifStackTable|1.3.6.1.2.1.31.1.2
ifStackEntry|ifStackEntry|1.3.6.1.2.1.31.1.2.1
ifStackHigherLayer|ifStackHigherLayer|1.3.6.1.2.1.31.1.2.1.1
ifStackLowerLayer|ifStackLowerLayer|1.3.6.1.2.1.31.1.2.1.2
ifStackStatus|ifStackStatus|1.3.6.1.2.1.31.1.2.1.3
ifTestTable|ifTestTable|1.3.6.1.2.1.31.1.3
ifTestEntry|ifTestEntry|1.3.6.1.2.1.31.1.3.1
ifTestId|ifTestId|1.3.6.1.2.1.31.1.3.1.1
ifTestStatus|ifTestStatus|1.3.6.1.2.1.31.1.3.1.2
ifTestType|ifTestType|1.3.6.1.2.1.31.1.3.1.3
ifTestResult|ifTestResult|1.3.6.1.2.1.31.1.3.1.4
ifTestCode|ifTestCode|1.3.6.1.2.1.31.1.3.1.5
ifTestOwner|ifTestOwner|1.3.6.1.2.1.31.1.3.1.6
ifRcvAddressTable|ifRcvAddressTable|1.3.6.1.2.1.31.1.4
ifRcvAddressEntry|ifRcvAddressEntry|1.3.6.1.2.1.31.1.4.1
ifRcvAddressAddress|ifRcvAddressAddress|1.3.6.1.2.1.31.1.4.1.1
ifRcvAddressStatus|ifRcvAddressStatus|1.3.6.1.2.1.31.1.4.1.2
ifRcvAddressType|ifRcvAddressType|1.3.6.1.2.1.31.1.4.1.3
ifTableLastChange|ifTableLastChange|1.3.6.1.2.1.31.1.5
ifStackLastChange|ifStackLastChange|1.3.6.1.2.1.31.1.6
ifConformance|ifConformance|1.3.6.1.2.1.31.2
ifGroups|ifGroups|1.3.6.1.2.1.31.2.1
ifGeneralGroup|ifGeneralGroup|1.3.6.1.2.1.31.2.1.1
ifGeneralInformationGroup|ifGeneralInformationGroup|1.3.6.1.2.1.31.2.1.10
ifStackGroup2|ifStackGroup2|1.3.6.1.2.1.31.2.1.11
ifOldObjectsGroup|ifOldObjectsGroup|1.3.6.1.2.1.31.2.1.12
ifCounterDiscontinuityGroup|ifCounterDiscontinuityGroup|1.3.6.1.2.1.31.2.1.13
linkUpDownNotificationsGroup|linkUpDownNotificationsGroup|1.3.6.1.2.1.31.2.1.14
ifFixedLengthGroup|ifFixedLengthGroup|1.3.6.1.2.1.31.2.1.2
ifHCFixedLengthGroup|ifHCFixedLengthGroup|1.3.6.1.2.1.31.2.1.3
ifPacketGroup|ifPacketGroup|1.3.6.1.2.1.31.2.1.4
ifHCPacketGroup|ifHCPacketGroup|1.3.6.1.2.1.31.2.1.5
ifVHCPacketGroup|ifVHCPacketGroup|1.3.6.1.2.1.31.2.1.6
ifRcvAddressGroup|ifRcvAddressGroup|1.3.6.1.2.1.31.2.1.7
ifTestGroup|ifTestGroup|1.3.6.1.2.1.31.2.1.8
ifStackGroup|ifStackGroup|1.3.6.1.2.1.31.2.1.9
ifCompliances|ifCompliances|1.3.6.1.2.1.31.2.2
ifCompliance|ifCompliance|1.3.6.1.2.1.31.2.2.1
ifCompliance2|ifCompliance2|1.3.6.1.2.1.31.2.2.2
ifCompliance3|ifCompliance3|1.3.6.1.2.1.31.2.2.3
linkDown|linkDown|1.3.6.1.6.3.1.1.5.3
linkUp|linkUp|1.3.6.1.6.3.1.1.5.4