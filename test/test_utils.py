import socket
import time
import pynmea2
import serial as serial
import pyautogui
#import pywin32
import os
import time
from PIL import Image
from PIL import ImageChops
import subprocess
import sys

from pywinauto import Application, win32defines
from pywinauto.win32functions import ShowWindow, SetFocus

class Nmea:

    @staticmethod
    def serial_stat(duration=10, device='/dev/ttyUSB0', baudrate=4800, log=""):
        """
        Setup serial port and record 10 seconds of NMEA data
        """
        nmea_statistic = {}

        # Open log file if needed
        if log != "":
            LogFile = open(log, 'w')
            LogFile.write("Log for Duration " + str(duration) + "sec on Port " + str(device) + " with " + str(baudrate) + " baud\n")

        with serial.Serial(device, baudrate=baudrate, timeout=1) as ser:

            # flush old nmea line
            message = ser.readline().decode('ascii', errors='replace')

            # Record NMEA data via UPD for 10sec to gather statistic data
            starttime = time.time()
            messtime = time.time()
            while (messtime - starttime) < duration:

                messtime = time.time()

                # skip if no data is available
                if ser.inWaiting() <= 0:
                    time.sleep(0.1)
                    continue


                # Get next NMEA sentence from UPD port
                message = ser.readline().decode('ascii', errors='replace')
                messtime = time.time()

                # Decode NMEA sentence
                try:
                    nmea_sentence = pynmea2.parse(message)
                except pynmea2.nmea.ChecksumError as error:
                    print("* %0004.2f \t * %s \t * %s* ^⁻-- Failure Checksum" % ((messtime - starttime), device, message))
                    continue
                except pynmea2.nmea.ParseError as error:
                    print("* %0004.2f \t * %s \t * %s* ^--- Failure Parsing" % ((messtime - starttime), device, message))
                    continue


                # Push NMEA sentence to statistic data struct
                if nmea_sentence.sentence_type not in nmea_statistic:
                    nmea_statistic[nmea_sentence.sentence_type] = []
                nmea_statistic[nmea_sentence.sentence_type].append(((messtime - starttime), nmea_sentence))

                if log != "":
                    LogFile.write("|  %004.2f \t | %s \t | %s \n" % ((messtime - starttime), device, nmea_sentence))

        # Close log file
        if log != "":
            LogFile.close()

        return nmea_statistic


    @staticmethod
    def udp_stat(duration=10, port=10110, log=""):
        """
        Setup UDP socket and record 10 seconds of NMEA data
        """
        nmea_statistic = {}

        # Open broadcast socket for port 10110
        NmeaSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        NmeaSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        NmeaSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        NmeaSocket.bind(('', port))
        message, address = NmeaSocket.recvfrom(8192)

        # Open log file if needed
        if log!="":
            LogFile = open(log, 'w')
            LogFile.write("Log for Duration " + str(duration) + "sec on Port " + str(port) + "\n")

        # Record NMEA data via UPD for 10sec to gather statistic data
        starttime = time.time()
        messtime  = time.time()
        while (messtime-starttime) < duration:
            # Get next NMEA sentence from UPD port
            message, address = NmeaSocket.recvfrom(8192)
            messtime = time.time()
            message = message.decode("ascii")
            message = '$' + message.split('$')[-1]

            # Decode NMEA sentence
            try:
                nmea_sentence = pynmea2.parse(message)
            except pynmea2.nmea.ChecksumError as error:
                print("* %0004.2f \t * %s* ^⁻-- Failure Checksum" % ((messtime - starttime), message))
                continue
            except pynmea2.nmea.ParseError as error:
                print("* %0004.2f \t * %s* ^--- Failure Parsing" % ((messtime - starttime),  message))
                continue

            # Push NMEA sentence to statistic data struct
            if nmea_sentence.sentence_type not in nmea_statistic:
                nmea_statistic[nmea_sentence.sentence_type] = []
            nmea_statistic[nmea_sentence.sentence_type].append(((messtime - starttime), nmea_sentence))

            if log != "":
                LogFile.write("|  %004.2f \t | %s \t | %s \n" % ((messtime - starttime), address, nmea_sentence))

        # Close UDP socket
        NmeaSocket.close()

        # Close log file
        if log != "":
            LogFile.close()

        return nmea_statistic

    @staticmethod
    def min_stat(statlist):
        min_value = 999

        if len(statlist) < 2:
            return 0

        for i in range(1,len(statlist)):
            diff = statlist[i][0]-statlist[i-1][0]
            min_value = min(min_value,diff)

        return min_value

    @staticmethod
    def max_stat(statlist):
        max_value = 0

        if len(statlist) < 2:
            return 0

        for i in range(1, len(statlist)):
            diff = statlist[i][0] - statlist[i - 1][0]
            max_value = max(max_value, diff)

        return max_value

    @staticmethod
    def mean_stat(statlist):
        akku_value = 0
        akku_cnt = 0

        for i in range(1, len(statlist)):
            akku_value = akku_value + statlist[i][0] - statlist[i - 1][0]
            akku_cnt = akku_cnt + 1

        res = akku_value / akku_cnt
        return res



if __name__ == '__main__':
    Nmea.udp_stat(10)
