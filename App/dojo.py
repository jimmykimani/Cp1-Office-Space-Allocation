"""
File      : dojo.py
Date      : March, 2017
Author(s) : Jimmy Kimani <jimmykkimani@gmail.com>
Desc      : Office Allocator model module
"""
# ============================================================================
# necessary imports
# ============================================================================
import random

from  App.person import Fellow, Staff
from  App.rooms import Livingspace, Office
from tabulate import tabulate
from colorama import Fore, Back, Style

class Dojo(object):

    def __init__(self):
        self.all_rooms = []
        self.fellows = []
        self.staff = []
        self.all_people = []
        self.livingspace = []
        self.office = []
        self.vacant_rooms = []
        self.vacant_offices = []
        self.vacant_livingspaces = []
        self.allocated = []
        self.allocated_people = []
        self.unallocated_people = []
        self.fellows = []
        self.allocated_fellows = []
        self.staff = []
        self.allocated_staff = []


    def create_room(self, name, type_room):
        ''' checks for duplicate room names'''
        room_names = [room.name for room in self.all_rooms]
        msg = ''
        if name in room_names:
            msg = "sorry, one or more room name's already exists!please choose another name"
            print(msg)
            return msg
        else:
            '''Create new Livingspace for person(s)'''
            if type_room.lower() == 'livingspace':
                new_room = Livingspace(name)
                self.livingspace.append(new_room)
                self.all_rooms.append(new_room)
                msg = ' A Livingspace called %s has been successfully created!' % new_room.name
                print (msg)

            elif type_room.lower() == 'office':
                new_room = Office(name)
                self.office.append(new_room)
                self.all_rooms.append(new_room)
                msg = ' An office called %s has been successfully created!' % new_room.name
                print (msg)
            else:
                print ('invalid')


    def check_vacant_rooms(self):
        ''' checks for vacant rooms'''
        for office in self.office:
            if len(office.members) < office.capacity:
                if office not in self.vacant_offices:
                    self.vacant_offices.append(office)
                    self.vacant_rooms.append(office)
            elif len(office.members) >= office.capacity:
                if office in self.vacant_offices:
                    self.vacant_offices.remove(office)
                    self.vacant_rooms.remove(office)
                    ''' checks vacant rooms and add to a list'''
        for livingspace in self.livingspace:
            if len(livingspace.members) < livingspace.capacity:
                if livingspace not in self.vacant_livingspaces:
                    self.vacant_livingspaces.append(livingspace)
                    self.vacant_rooms.append(livingspace)
                elif len(livingspace.members) >= livingspace.capacity:
                    if livingspace in self.vacant_livingspaces:
                        self.vacant_livingspaces.append(livingspace)
                        self.vacant_rooms.append(livingspace)

    def add_person(self, name, category, wants_accomodation= 'N'):
        """Add new person"""
        if category == 'fellow':
            new_person = Fellow(name)
            if wants_accomodation == 'Y':
                ''' checks for vacant room'''
                if self.livingspace:
                    self.check_vacant_rooms()
                    if not self.vacant_livingspaces:
                        print('there no rooms at the moment')
                        return
                    else:
                        ''' chooses a random room to a user'''
                        lspace_choice = random.choice(self.vacant_livingspaces)
                        lspace_choice.members.append(new_person)
                        self.fellows.append(new_person)
                        self.all_people.append(new_person)
                        msg = 'Fellow %s has been successfully added and assigned to Livingspace %s !' % (new_person.name, lspace_choice.name)
                        print (msg)
                        return (msg)
                        ''' Error message if room is not created'''
                    print ('There no rooms, please add one by using the create room command')
            else:
                if self.office:
                    self.check_vacant_rooms()
                    if not self.vacant_offices:
                        print ( 'There are no rooms available at the moment')
                        return
                    else:
                        office_choice = random.choice(self.vacant_offices)
                        ''' Adds user to room mebers list'''
                        office_choice.members.append(new_person)
                        self.fellows.append(new_person)
                        self.all_people.append(new_person)
                        self.allocated_fellows.append(new_person)
                        msg = 'Fellow %s has been successfully added and assigned to office %s !' % (new_person.name, office_choice.name)
                        print (msg)
                        return (msg)
                    print ('There no rooms, please add one by using the create room command')
        elif category == 'staff':
            new_person = Staff(name)
            if self.office:
                self.check_vacant_rooms()
                if not self.vacant_offices:
                    print ('no offices')
                    return
                else:
                    office_choice = random.choice(self.vacant_offices)
                    new_person = Staff(name)
                    office_choice.members.append(new_person)
                    self.staff.append(new_person)
                    self.all_people.append(new_person)
                    self.allocated_staff.append(new_person)
                    msg = 'Staff %s has been successfully added and assigned to office %s' % (new_person.name, office_choice.name)
                    print (msg)
            else:
                print ('There no rooms, please add one by using the create room command')

    def print_room(self, room_name):
        rooms = self.all_rooms
        table_headers = ['room','member']
        ''' empty table list for name'''
        table = []
        for room in rooms:
            if room_name == room_name:
                for member in room.members:
                    #  Adds item to empty list
                    table.append([room_name, member.name])
                    print (Fore.YELLOW + tabulate(table, table_headers, tablefmt="grid"))
            else:
                return ' add name'
        else:
            print 'no room found! please add one by using the create_room command'
                
                    # print (member.name)
        
    def print_unallocated(self, filename):
        pass
    def print_allocations(self, filename):
        pass
            