import array
import os
import json
import time

import ntptime
from machine import Pin,PWM, UART
from umodbus.serial import Serial as ModbusRTUMaster
import rp2
import network
from umqtt.simple import MQTTClient
import network
import socket
import usocket
import struct

from secret import ssid, password
import socket
import gc

led = Pin("LED", Pin.OUT)
led.on()
# time.sleep(15)
led.off()



id = ""
for b in machine.unique_id():
  id += "{:02X}".format(b)
# id ='E6616408439B5233'
print("id", id)
# 
# SUBSCRIBED_CHANNEL=b'id'+id+'/#'
# SUBSCRIBED_CHANNEL1=b'id'+id+'/Switches'
# SUBSCRIBED_CHANNEL2=b'id'+id+'/ModBusSend'
# 
# 
# 
# print("SUBS CHANNELS",SUBSCRIBED_CHANNEL)
# print("SUBS CHANNELS1",SUBSCRIBED_CHANNEL1)
# print("SUBS CHANNELS2",SUBSCRIBED_CHANNEL2)
# CLIENT_ID = id
# modbus_cmd_rcv=0
# 
# 
# 
# def get_ssl_params():
#     """ Get ssl parameters for MQTT"""
#     # These keys must be in der format the keys
#     # downloaded from AWS website is in pem format
#     keyfile = '/certs/private.der'
#     with open(keyfile, 'rb') as f:
#         key = f.read()
#     certfile = "/certs/certificate.der"
#     with open(certfile, 'rb') as f:
#         cert = f.read()    
#     ssl_params = {'key': key,'cert': cert, 'server_side': False}
#     return ssl_params
# 
# def mqtt_callback(topic, msg):
#     global flag
#     """ Callback function for received messages"""
#     print("received data:")
#     topicd = topic.decode('utf-8')
#     msgd = msg.decode('utf-8')
#     print("topic: %s message: %s" %(topicd, msgd))
#     log_msg("Message Received", format_time(now), id)
#     
#     modbus_cmd_rcv=0
#     if topic==SUBSCRIBED_CHANNEL1:
#         # on pico w in is connected to wireless chip so led code must adept to it
#         response = msgd
# #         send_disp_msg(response)
#         ("P2", response)
#         f = open('switches.txt', 'w')
#         f.write(response)
#         f.close()
#     if topic==SUBSCRIBED_CHANNEL2:
#         modbus_cmd_rcv=1
#         # on pico w in is connected to wireless chip so led code must adept to it
#         response = msgd
# #         send_disp_msg(response)
#         print("P2", response, "MCR", modbus_cmd_rcv)
#         f = open('modbuscmd.txt', 'w')
#         f.write(response)
#         f.close()
#     else: modbus_cmd_rcv=0
#     print("about to return" ,modbus_cmd_rcv)
#     return modbus_cmd_rcv
#     
#  
# def connect():
#     #Connect to WLAN
#     wlan = network.WLAN(network.STA_IF)
#     wlan.active(True)
#     wlan.connect(ssid, password)
#     while wlan.isconnected() == False:
#         print('Waiting for connection...')
#         print(ssid, password)
#         led.on()
#         time.sleep(6)
#         led.off()
#     print(wlan.ifconfig())
# try:
#     logfull=1
#     try:
#         connect()
#     except KeyboardInterrupt:
#         machine.et()
#         
# 
# #     log_msg("WifiConnected", format_time(now), id)    
#     timenow=time.localtime()
#     currstat=''
#     print("Time 1", timenow)
#     n=0
#     while n==0:
#         try: 
#             ntptime.settime()
#             n=1
#         except:
#             print("NTP Timed out, will retry")
#             continue
# 
#         
#     now=time.localtime()
#     print("Time 2", now)
# 
#     print("Output", format_time(now))
#     print("UNIX", time.time())
#     print("UNIX 2", time.time()+1209600)
#     
#     ssl_params=get_ssl_params()
# 
#     print("Just prior to MQTT")
#     # Connect to MQTT broker.
#     mqtt = MQTTClient( CLIENT_ID, AWS_ENDPOINT, port = 8883, keepalive = 1200, ssl = True, ssl_params = ssl_params )
#     mcr=mqtt.set_callback(mqtt_callback)
#     print("MCR", mcr)
#     print("A")
#     mqtt.connect()
#     print("B")
#     mqtt.subscribe(SUBSCRIBED_CHANNEL)
# 
#     print("C")
#     log_msg("Succesful Startup", format_time(now), id)
# 
#     # Send 2 messages to test publish messages
#     print("Sending messages...")
#     for i in range(2):
#         mqtt.publish( topic = PUBLISH_CHANNEL, msg = b'{"temp":%s}' , qos = 0 )
#         time.sleep_ms(2000)
#         print("done sending messages waiting for messages...")
#         if logfull==1:
#             now=time.localtime()
#             formatnow=format_time(now)
#             log_msg('published first messages', formatnow, id)
#         
#         
#     rtu_pins = (0, 1)         # (TX, RX)
# #         uart_id = 1
# #         uart0 = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))
#     a=0
#     ch0 = ModbusRTUMaster(
#         pins=rtu_pins,          # given as tuple (TX, RX)
#         # baudrate=9600,        # optional, default 9600
#         # data_bits=8,          # optional, default 8
#         # stop_bits=1,          # optional, default 1
#         # parity=None,          # optional, default None
#         # ctrl_pin=12,          # optional, control DE/RE
#         uart_id=0        # optional, default 1, see port specific documentation
#     )
#     rtu_pins = (4, 5)         # (TX, RX)
# #         uart_id = 1
# #         uart0 = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))
#     a=0
#     ch1 = ModbusRTUMaster(
#         pins=rtu_pins,          # given as tuple (TX, RX)
#         # baudrate=9600,        # optional, default 9600
#         # data_bits=8,          # optional, default 8
#         # stop_bits=1,          # optional, default 1
#         # parity=None,          # optional, default None
#         # ctrl_pin=12,          # optional, control DE/RE
#         uart_id=1		        # optional, default 1, see port specific documentation
#     )
#    
#     slave_addr=0x01
#     slave_addr_2=0x02
# 
#     output_address1=0x00
#     output_address2=0x01
#     output_address3=0x02
#     output_address4=0x03
#     output_address5=0x04
#     output_address6=0x05
#     output_address7=0x06
#     output_address8=0x07
#     output_address9=0x08
#     output_address10=0x09
#     output_address11=0x0A
#     output_address12=0x0B
#     output_address13=0x0C
#     output_address14=0x0D
#     output_address15=0x0E
#     output_address16=0x0F
#     output_address_hppower=0x0305
#     output_address_hpmode=0x0304
#     
#     read_address=0x000
#     output_value_on=0xFF00
#     output_value_off=0x0000
#     output_value_hp_on=0x0001
#     output_value_hp_off=0x0000
#     output_value_hp_water=0x0002
#     output_value_hp_heat=0x0001
#     output_value_hp_cool=0x0000
#     query_addresses=[0x0,0x1,0x2,0x3,0x4,0x4A,0x4B,0x4F,0x50,0x58,0x5C,0x5D,0x54,0x40,0x41]
#     query_names=['RS1','RS2','ES1','ES2','ES3','AmbTemp','CoilTemp','InTemp','OutTemp','Flow','InKWH','kwhCon', 'TankTemp',"CompFreq", "FanFreq"]
#     query_resps=['','','','','','','','','','','','','','','']
#     
#     cool_query_addresses=[0x0,0x1,0x2,0x3,0x4,0x8, 0x9, 0xA]
#     cool_query_names=['CPOWER','CFANSP','CMODE','CTEMP','CLOCK','CROOM','CVALVE','CFANST']
#     cool_query_resps=['','','','','','','','']
#     cool_on_addresses=[0x0,0x1,0x2,0x3]
#     cool_on_values=[1,0,0,170]
#     cool_off_addresses=[0x0,0x1,0x2,0x3]
#     cool_off_values=[0,0,0,250]        
#         
# 
#     while True:
# # Main Loop Starts here
#         for k in range(10):
# # This loop occurs once a minute and is where we check new switch files
#             print("MqttC3")
#             if logfull==1:
#                 now=time.localtime()
#                 formatnow=format_time(now)
#                 log_msg('About to check for messages', formatnow, id)
#                     
#             mqtt.check_msg()
#             if logfull==1:
#                 now=time.localtime()
#                 formatnow=format_time(now)
#                 log_msg('Checked messages', formatnow, id)            
#             
#             timenow=time.localtime()
#             print("k", k, timenow)
#             #inner loop do every minute 
#             #Check for messages from MQTT
#             print("//////")
#             gc.collect()
#             x=gc.mem_free()
# 
#             fileexists = None
#             while fileexists is None:
# # Try to open the switches file
#                 try:
#                     print("Attempt Open")
#                     print("MCR", modbus_cmd_rcv)
#                     f = open('switches.txt')
#                     if logfull==1:
#                         now=time.localtime()
#                         formatnow=format_time(now)
#                         log_msg('File Opened', formatnow, id)                    
#                     fileexists = 'Y'                    
#                 except OSError:
#                     print("No File Exists")
#                     now=time.localtime()
#                     formatnow=format_time(now)
#                     log_msg('Device has no switches file onboard', formatnow, id)
#                     time.sleep(60)
#                     print("MqttC1")
#                     mqtt.check_msg()
#             filevalid = None
#             while filevalid is None:
# # Try to read the switches file, checking structure                
#                 try:
#                     data = json.load(f)
#                     now=time.localtime()
#                     formatnow=format_time(now)
#                     print("formatnow", formatnow)
#                     checktime = '2000-00-00 00:00:00'
#                     filedets=data['ResponseMetadata']
#                     fileid=filedets['RequestId']
#                     print("File ID", fileid)
#                     pub_fileid(fileid)
#                     filevalid = 'Y'
#                     if logfull==1:
#                         now=time.localtime()
#                         formatnow=format_time(now)
#                         log_msg('File Has Valid Data', formatnow, id)                    
#                     print("Result 4 set")
#                 except OSError:
#                     print("Invalid file")
#                     now=time.localtime()
#                     formatnow=format_time(now)
#                     log_msg('Invalid file 1', formatnow, id)
#                     time.sleep(60)
#                     print("MqttC2")
#                     mqtt.check_msg()
#                     f = open('switches.txt')            
#             mainloop = None
#             while mainloop is None:
#                 print("In Main Loop")
#                 try:
#                     for i in data['Items']:
# # Loop through switches until you fin latest past switch on time
# #                         print(i['STime'])
# #                         print("The time in the switch file is", i['STime'])
# #                         print("And the time now is", formatnow)
#                         if i['STime'] < formatnow:
# #                             print("This command is in the past")
# #                             print("And the current checktime is", checktime)
#                             if i['STime'] > checktime:
#                                 checktime = i['STime']
#                                 switchstring=i['AllSwitch']
# #                                 print("and this is now the latest switch in the past", checktime)
#                                 sw1=switchstring[0]
#                                 flagarray[0]=sw1
#                                 sw2=switchstring[1]
#                                 flagarray[1]=sw2
#                                 sw3=switchstring[2]
#                                 flagarray[2]=sw3
#                                 sw4=switchstring[3]
#                                 flagarray[3]=sw4
#                                 sw5=switchstring[4]
#                                 flagarray[4]=sw5
#                                 sw6=switchstring[5]
#                                 flagarray[5]=sw6
#                                 sw7=switchstring[6]
#                                 flagarray[6]=sw7
#                                 sw8=switchstring[7]
#                                 flagarray[7]=sw8
#                                 sw9=switchstring[8]
#                                 flagarray[8]=sw9
#                                 sw10=switchstring[9]
#                                 flagarray[9]=sw10
#                                 sw11=switchstring[10]
#                                 flagarray[10]=sw11
# #                                 sw12=i['S12']
# #                                 flagarray[11]=sw12                                
# #                                 sw13=i['S13']
# #                                 flagarray[12]=sw13                               
# #                                 sw14=i['S14']
# #                                 flagarray[13]=sw14                                
# #                                 sw15=i['S15']
# #                                 flagarray[14]=sw15                                
# #                                 sw16=i['S16']
# #                                 flagarray[15]=sw16                                
#                                 sw17=switchstring[16]
#                                 flagarray[16]=sw17                                
#                                 currstat = i['SStatus']
#                     print("time to be used", checktime)
# #Now decide what to do given this switch config                    
# #                     print("flagarray",flagarray)
# #First part just creates log entry
#                     flagtext=''
#                     num=0
#                     for i in  flagarray:
# #                         print("CH",flagarray[num])
#                         flagtext+=str(flagarray[num])                     
#                         num+=1
#                     print("Curr Stat", currstat)
#                     log_msg(k+"Stat"+flagtext+currstat, formatnow, id)
#                     
# # Is the flag array different from last one implemented                    
#                     if flagarray==prevflagarray:
#                         pass           
#                         print("No Change to switches")
#                     else:
# # Implement new switches
#                         m_signed=True
#                         if sw1=='T':
#                             return_flag = ch0.write_single_coil(slave_addr, output_address1, output_value_on)
#                         else: return_flag = ch0.write_single_coil(slave_addr, output_address1, output_value_off)
#                         if sw2=='T':
#                             return_flag = ch0.write_single_coil(slave_addr, output_address2, output_value_on)
#                         else: return_flag = ch0.write_single_coil(slave_addr, output_address2, output_value_off)
#                         if sw3=='T':
#                             return_flag = ch0.write_single_coil(slave_addr, output_address3, output_value_on)
#                         else: return_flag = ch0.write_single_coil(slave_addr, output_address3, output_value_off)
#                         if sw4=='T':
#                             return_flag = ch0.write_single_coil(slave_addr, output_address4, output_value_on)
#                         else: return_flag = ch0.write_single_coil(slave_addr, output_address4, output_value_off)
#                         if sw5=='T':
#                             return_flag = ch0.write_single_coil(slave_addr, output_address5, output_value_on)
#                         else: return_flag = ch0.write_single_coil(slave_addr, output_address5, output_value_off)
#                         if sw6=='T':
#                             return_flag = ch0.write_single_coil(slave_addr, output_address6, output_value_on)
#                         else: return_flag = ch0.write_single_coil(slave_addr, output_address6, output_value_off)
#                         if sw7=='T':
#                             return_flag = ch0.write_single_coil(slave_addr, output_address7, output_value_on)
#                         else: return_flag = ch0.write_single_coil(slave_addr, output_address7, output_value_off)
#                         if sw8=='T':
#                             return_flag = ch0.write_single_coil(slave_addr, output_address8, output_value_on)
# 
#                         else: return_flag = ch0.write_single_coil(slave_addr, output_address8, output_value_off)
#                         if sw9=='T':
#                             return_flag = ch0.write_single_coil(slave_addr, output_address9, output_value_on)
#                         else: return_flag = ch0.write_single_coil(slave_addr, output_address9, output_value_off)
#                         if sw10=='T':
#                             return_flag = ch0.write_single_coil(slave_addr, output_address10, output_value_on)
#                         else: return_flag = ch0.write_single_coil(slave_addr, output_address10, output_value_off)
#                         if sw11=='T':
#                             return_flag = ch0.write_single_coil(slave_addr, output_address11, output_value_on)
#                         else: return_flag = ch0.write_single_coil(slave_addr, output_address11, output_value_off)
# #                         if sw12=='T':
# #                             return_flag = ch0.write_single_coil(slave_addr, output_address12, output_value_on)
# #                         else: return_flag = ch0.write_single_coil(slave_addr, output_address12, output_value_off)
# #                         if sw13=='T':
# #                             return_flag = ch0.write_single_coil(slave_addr, output_address13, output_value_on)
# #                         else: return_flag = ch0.write_single_coil(slave_addr, output_address13, output_value_off)
# #                         if sw14=='T':
# #                             return_flag = ch0.write_single_coil(slave_addr, output_address14, output_value_on)
# #                         else: return_flag = ch0.write_single_coil(slave_addr, output_address14, output_value_off)
# #                         if sw15=='T':
# #                             return_flag = ch0.write_single_coil(slave_addr, output_address15, output_value_on)
# #                         else: return_flag = ch0.write_single_coil(slave_addr, output_address15, output_value_off)
#                         if sw17=='C':
#                             print("Cooling to be done")
#                             return_flag = ch1.write_single_register(slave_addr, output_address_hppower, output_value_hp_on, m_signed)
#                             return_flag = ch1.write_single_register(slave_addr, output_address_hpmode, output_value_hp_cool, m_signed)
#                             for j in range(0, len(cool_on_addresses)):
#                                 print("About to set reg", cool_on_addresses[j], "to", cool_on_values[j])
#                                 return_flag = ch0.write_single_register(slave_addr_2,cool_on_addresses[j], cool_on_values[j], m_signed)
#                                 time.sleep(1)
#                                 print("Cooling Done")
#                         else:
#                             print("Cooling Off")
#                             return_flag = ch1.write_single_register(slave_addr, output_address_hppower, output_value_hp_off, m_signed)
#                             for j in range(0, len(cool_off_addresses)):
#                                 return_flag = ch0.write_single_register(slave_addr_2,cool_off_addresses[j], cool_off_values[j], m_signed)
# #                                         time.sleep(1)
#                         
#                         if sw17=='W':
#                             return_flag = ch1.write_single_register(slave_addr, output_address_hppower, output_value_hp_on, m_signed)
#                             return_flag = ch1.write_single_register(slave_addr, output_address_hpmode, output_value_hp_water, m_signed)
#                         else:
#                             if sw17=='H':
#                                 return_flag = ch1.write_single_register(slave_addr, output_address_hppower, output_value_hp_on, m_signed)
#                                 return_flag = ch1.write_single_register(slave_addr, output_address_hpmode, output_value_hp_heat, m_signed)
# 
#                         now=time.localtime()
#                         formatnow=format_time(now)
#                         log_msg('Switches Changed '+currstat, formatnow, id)
#                         
#                         for j in range(0, len(flagarray)): 
#                             prevflagarray[j]=flagarray[j]
# # Below runs whether new switches or not
#                     f.close()
#                     try:
#                         m_signed=True
#                         m = open('modbuscmd.txt')
# #If new ad hoc modbus command has been sent process it and delete request
#                         datamod = json.load(m)
#                         print("Doing modbus ad hoc")
#                         for i in datamod['content']:
#                             modmode=i['mode']
#                             if modmode=='Update':
#                                 try:
#                                     print("Doing update")
#                                     maddress_updt=i['address']
#                                     maddress_updt_int=int(maddress_updt, 16)
#                                     maddress_updt_hex=hex(maddress_updt_int)
#                                     print("MAUH", maddress_updt_hex)
#                                     mcontent_updt=i['command']
#                                     mcontent_updt_int=int(mcontent_updt)
#                                     print("MCUI", mcontent_updt_int)
#                                     return_flag = ch1.write_single_register(slave_addr, maddress_updt_int, mcontent_updt_int, m_signed)
#                                     print("Return Flag", return_flag)
#                                 except Exception as e:
#                                     print("Update exception", e)
#                                     
#                             if modmode=='Query':
#                                 try:
#                                     print("Doing query")
#                                     maddress_query=i['address']
#                                     maddress_query_int=int(maddress_query, 16)
#                                     print("MAQI",hex(maddress_query_int))                                  
#                                     mregnum_query=i['registersnum']
#                                     mregnum_query_int=int(mregnum_query)
#                                     print("MRQI",mregnum_query_int)
#                                     register_value = ch1.read_holding_registers(slave_addr, maddress_query_int, mregnum_query_int, m_signed)
#                                     print('Status of Reg {}: {}'.format(maddress_query_int, register_value))
#                                     reg_to_publish = (hex(maddress_query_int), mregnum_query_int,  register_value)
#                                     now=time.localtime()
#                                     exp = time.time()+1209600 
#                                     formatnow=format_time(now)
#                                     print("Publish 5")
#                                     my_json_string_modbus = json.dumps({'Device': id, 'Timestamp': formatnow, 'Message': reg_to_publish, 'Expiry': exp })
#                                     mqtt.publish( topic = PUBLISH_CHANNEL_MODBUS, msg = my_json_string_modbus , qos = 0 )
#                                 except Exception as e:
#                                     print("Update exception", e)
#                             if modmode=='WaterOn':
#                                 try:
#                                     print("Switching On Water Tap")
#                                     return_flag = ch0.write_single_coil(slave_addr, output_address10, output_value_on)
#                                     log_msg('WaterTapOn', formatnow, id)
#                                 except Exception as e:
#                                     print("Update exception", e)
#                             if modmode=='WaterOff':
#                                 try:
#                                     print("Switching Off Water Tap")
#                                     return_flag = ch0.write_single_coil(slave_addr, output_address10, output_value_off)
#                                     log_msg('WaterTapOff', formatnow, id)
#                                 except Exception as e:
#                                     print("Update exception", e)
#                         m.close()
#                         os.remove("modbuscmd.txt")
#                     except:
#                         print("No Modbus Cmd")
# # Do regular modbus query
#                     querydata=''
#                     try:
#                         m_signed=True
#                         print("Main MOdbus Query Section")
#                         for l in range(6):
# #                             print("++++")
#                             timenow=time.localtime()
# #                             print("l", l, timenow)
#                             for j in range(0, len(query_addresses)):
#                                 register_value = ch1.read_holding_registers(slave_addr, query_addresses[j], 1, m_signed)                               
#                                 query_resps[j]=register_value
# #                                 print(query_addresses[j], register_value, j)
#                             querydata = {"content": []}
#        
#                             
#                             for j in range(0, len(query_addresses)):
# #                                 print("In Range 2", j)
#                                 if query_names[j]=='RS1':
#                                     stat_out=query_resps[j]
# #                                     print("SO", stat_out, type(stat_out))
#                                     stat_out_one = stat_out[0]
# #                                     print("SO1", stat_out_one, type(stat_out_one))
#                                 querydata["content"].append({
#                                     "query_name": query_names[j],
#                                     "query_reg": query_addresses[j], 
#                                     "query_res": query_resps[j], 
#                                 })
# #                                 print ("The original number is : " + str(test_num))
# #                             print("Pre Res", stat_out_one)
#                             res = [int(i) for i in list('{0:0b}'.format(stat_out_one))]
# #                             print("the 9th last digit is", res[-9] )
#                             m=0
#                             print("res", res, len(res))
#                             if len(res)>=9:
#                                 if res[-9]==1:
# # Defrost mode logic, switches hp and gas boiler on to do defrost, runs for 300 second cycles
#                                     timenow=time.localtime()
#                                     print("m", m, timenow)
#                                     while m<300:
#                                         # do gas heating or water here
#                                         # sleep for 75 secs
#                                         # need to not trigger again for eg 5 mins?
#                                         if m==0:
#                                             print("M=0")
#                                             if currstat == 'HP Water':
#                                                 return_flag = ch0.write_single_coil(slave_addr, output_address2, output_value_on)
#                                             if currstat == 'HP Heat L':
#                                                 return_flag = ch0.write_single_coil(slave_addr, output_address1, output_value_on)
#                                         if m in (0,60,120,180,240,299):
#                                             timenow=time.localtime()
#                                             print("m60s", m, timenow)
#                                             for j in range(0, len(query_addresses)):      
#                                                 register_value = ch1.read_holding_registers(slave_addr, query_addresses[j], 1, m_signed)
#                                                 query_resps[j]=register_value
#                                             querydata = {"content": []}
#                                             for j in range(0, len(query_addresses)):
#                                                 if query_names[j]=='RS1':
#                                                     stat_out=query_resps[j]
#                                                 querydata["content"].append({
#                                                     "query_name": query_names[j],
#                                                     "query_reg": query_addresses[j], 
#                                                     "query_res": query_resps[j], 
#                                                 })
#                                             query_json_string = json.dumps(querydata)
#                                             print("Publish 1")
#                                             mqtt.publish(topic = PUBLISH_CHANNEL_QUERY, msg = query_json_string , qos = 0 )                                                                       
#                                         if m == 241:
#                                             timenow=time.localtime()
#                                             print("m241", m, timenow)                                        
#                                             if currstat == 'HP Water':
#                                                 return_flag = ch0.write_single_coil(slave_addr, output_address2, output_value_off)
#                                             if currstat == 'HP Heat L':
#                                                 return_flag = ch0.write_single_coil(slave_addr, output_address1, output_value_off)
#                                             now=time.localtime()
#                                             formatnow=format_time(now)
#                                             log_msg('Defrost Mode', formatnow, id)                                            
#                                         time.sleep(1)
#                                         m+=1
#                             time.sleep(10)
#                     except Exception as e:
#                         print("Unable to run Modbus Queries")
#                         print("Uncaught exception", e)
#                         now=time.localtime()
#                         formatnow=format_time(now)
#                         log_msg('Error in Reg Modbus Polling', formatnow, id)
#                         time.sleep(30)
#                     if querydata!='':
# # Assuming weve had a main modbus response above, do cooling modbus query and publish both
#                         query_json_string = json.dumps(querydata)                    
#                         for j in range(0, len(cool_query_addresses)):
# #                             print("Reg", cool_query_addresses[j])
#                             register_value = ch0.read_holding_registers(slave_addr_2, cool_query_addresses[j], 1, m_signed)
#                             cool_query_resps[j]=register_value
#                         cool_querydata = {"content": []}
#                         for j in range(0, len(cool_query_addresses)):
# 
#                             cool_querydata["content"].append({
#                                 "query_name": cool_query_names[j],
#                                 "query_reg": cool_query_addresses[j], 
#                                 "query_res": cool_query_resps[j], 
#                             })
#                         cool_query_json_string = json.dumps(cool_querydata)
#                         print("Publish 1 Cool")
#                         mqtt.publish(topic = COOL_PUBLISH_CHANNEL_QUERY, msg = cool_query_json_string , qos = 0 )                       
#                         mqtt.publish( topic = PUBLISH_CHANNEL_QUERY, msg = query_json_string , qos = 0 )
#                     mainloop='Y'
#                     now=time.localtime()
#                     formatnow=format_time(now)
#                     log_msg('Inner Loop OK',formatnow ,id)    
#                 except Exception as e:
#                     print("Uncaught exception", e)
#                     now=time.localtime()
#                     print("Now",now)
#                     formatnow=format_time(now)
#                     print("Formatnow",formatnow)
#                 #     log_msg(e,formatnow ,id)
#                     print("Logged")
#                     time.sleep(5)
#                     machine.reset()
#                 k+=1
#                 print("Inner k loop")
#         print("Outer")
#         now=time.localtime()
#         formatnow=format_time(now)
#         log_msg('All OK Outer Loop' + currstat + "/" + fileid, formatnow, id)
# 
# 
# 
# except Exception as e:
#     print("Uncaught exception", e)
#     now=time.localtime()
#     print("Now",now)
#     formatnow=format_time(now)
#     print("Formatnow",formatnow)
# #     log_msg(e,formatnow ,id)
#     print("Logged")
#     time.sleep(5)
#     machine.reset()
# #     
# 
# 
# 
# 
# 
# 
# 








