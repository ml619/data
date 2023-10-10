import pandas as pd
import h5py
import os


with h5py.File('data.h5', "a") as f:
    print("Keys: %s" % list(f.keys()))
    data_set = f[list(f.keys())[0]]
    data_set["Title"] = "noise in city station west"
    data_set["Subject"] = "the disruptive noises heard in city station west"
    data_set["Description"] = """
    Time is recorded in month day year format.
    There are 5 types of events in the event column. Sound events are in lowercase and describe the sound heard at that time
    The second type of event refers to the time when the recorder puts headphones on, denoted by \'HEADPHONES ON\' in the event column.
    The third type of event refers to the time when the recorder takes their headphones off, denoted by \'HEADPHONES OFF\' in the event column.
    The fourth type of event refers to when the recorder leaves the building denoted by \'LEFT\' in the event column.
    The fifth type of event refers to when a sound stopped denoted by \'STOP\' followed by \'-\' then the sounds row number in the event column.
    The data was first recorded on paper then entered into a laptop and afterward uploaded to github. The current owner is Michael Lenyszyn and ownership has not changed
    yet. The data was recorded from room 214 in city station west. Sound was recorded whenever the recorder heard a noise they
    would consider disruptive. The data was recorded in order to identify at which times there are
    the least disruptive noises in city station.
    """
    data_set["Creator"] = "Michael Lenyszyn"
    data_set["Publisher"] = "Michael Lenyszyn"
    data_set["Date"] = "September 28, 2023"
    data_set["Type"] = "description and time of sounds"
    data_set["Format"] = "HDF5"
    data_set["Identifier"] = "noise in city station west by Michael Lenyszyn"
    data_set["Source"] = "None"
    data_set["Language"] = "en"
    data_set["Relation"] = "None"
    data_set["Coverage"] = "City Station West, 1521 6th Ave, Troy, NY 12180"
    data_set["Rights"] = "Public Domain"