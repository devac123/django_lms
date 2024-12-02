from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from slotify.slotifyModels.SlotifyUserData import SlotifyUserData


@login_required
def SlotifyDashboard(req):
    user_id = req.user.id
    userData = SlotifyUserData.objects.filter(user_id=user_id)
    # Directly set content based on whether userData exists
    servic_entry() # creating dummu service
    slots_entry()  # creting dummy slots of that services  
    context = {
        'data': {
            'user': req.user,
            'userData': userData if userData.exists() else None    
        }
    }
    return render(req, 'slotify/SlotifyDashboard.html', context)  


def servic_entry():
    services = [
            {
                "name": "Doctor Appointment",
                "description": "Consult with a general physician.",
                "duration": 30,
                "price": 50.00
            },
            {
                "name": "Yoga Class",
                "description": "Join a relaxing yoga session.",
                "duration": 60,
                "price": 15.00
            },
            {
                "name": "Physiotherapy",
                "description": "Recover with expert physiotherapy.",
                "duration": 45,
                "price": 40.00
            },
            {
                "name": "Haircut",
                "description": "Professional haircut service.",
                "duration": 30,
                "price": 30.00
            },
            {
                "name": "Spa Therapy",
                "description": "Relax with a rejuvenating spa session.",
                "duration": 90,
                "price": 100.00
            },
            {
                "name": "Bridal Makeup",
                "description": "Perfect makeup for your special day.",
                "duration": 120,
                "price": 200.00
            },
            {
                "name": "DJ Service",
                "description": "Professional DJ for parties and events.",
                "duration": 240,
                "price": 500.00
            },
            {
                "name": "Catering",
                "description": "Delicious food catering for events.",
                "duration": 180,
                "price": 1000.00
            },
            {
                "name": "Photography",
                "description": "Capture moments with professional photography.",
                "duration": 120,
                "price": 300.00
            }
        ]
    for service_data in services:
        ser = SlotifyService.objects.filter(name = service_data["name"])
        if ser.count() == 0: 
            service = SlotifyService.objects.create(
                name=service_data["name"],
                description=service_data["description"],
                duration=service_data["duration"],
                price=service_data["price"]
            )

def slots_entry(): 
    slots1 =[{
        "Doctor Appointment": [
        {
            "id": 41,
            "start_time": "2024-12-14T09:00:00",
            "end_time": "2024-12-14T09:30:00",
            "is_available": True
        },
        {
            "id": 42,
            "start_time": "2024-12-14T09:30:00",
            "end_time": "2024-12-14T10:00:00",
            "is_available": True
        },
        {
            "id": 43,
            "start_time": "2024-12-14T10:00:00",
            "end_time": "2024-12-14T10:30:00",
            "is_available": True
        },
        {
            "id": 44,
            "start_time": "2024-12-14T10:30:00",
            "end_time": "2024-12-14T11:00:00",
            "is_available": True
        },
        {
            "id": 45,
            "start_time": "2024-12-14T11:00:00",
            "end_time": "2024-12-14T11:30:00",
            "is_available": True
        },
        {
            "id": 46,
            "start_time": "2024-12-14T11:30:00",
            "end_time": "2024-12-14T12:00:00",
            "is_available": True
        },
        {
            "id": 47,
            "start_time": "2024-12-14T12:00:00",
            "end_time": "2024-12-14T12:30:00",
            "is_available": True
        },
        {
            "id": 48,
            "start_time": "2024-12-14T12:30:00",
            "end_time": "2024-12-14T13:00:00",
            "is_available": True
        },
        {
            "id": 49,
            "start_time": "2024-12-14T13:00:00",
            "end_time": "2024-12-14T13:30:00",
            "is_available": True
        },
        {
            "id": 50,
            "start_time": "2024-12-14T13:30:00",
            "end_time": "2024-12-14T14:00:00",
            "is_available": True
        }
        ]
    },
    {
        "Yoga Class": [
        {
            "id": 51,
            "start_time": "2024-12-15T08:00:00",
            "end_time": "2024-12-15T09:00:00",
            "is_available": True
        },
        {
            "id": 52,
            "start_time": "2024-12-15T09:00:00",
            "end_time": "2024-12-15T10:00:00",
            "is_available": True
        },
        {
            "id": 53,
            "start_time": "2024-12-15T10:00:00",
            "end_time": "2024-12-15T11:00:00",
            "is_available": True
        },
        {
            "id": 54,
            "start_time": "2024-12-15T11:00:00",
            "end_time": "2024-12-15T12:00:00",
            "is_available": True
        },
        {
            "id": 55,
            "start_time": "2024-12-15T12:00:00",
            "end_time": "2024-12-15T13:00:00",
            "is_available": True
        },
        {
            "id": 56,
            "start_time": "2024-12-15T13:00:00",
            "end_time": "2024-12-15T14:00:00",
            "is_available": True
        },
        {
            "id": 57,
            "start_time": "2024-12-15T14:00:00",
            "end_time": "2024-12-15T15:00:00",
            "is_available": True
        },
        {
            "id": 58,
            "start_time": "2024-12-15T15:00:00",
            "end_time": "2024-12-15T16:00:00",
            "is_available": True
        },
        {
            "id": 59,
            "start_time": "2024-12-15T16:00:00",
            "end_time": "2024-12-15T17:00:00",
            "is_available": True
        },
        {
            "id": 60,
            "start_time": "2024-12-15T17:00:00",
            "end_time": "2024-12-15T18:00:00",
            "is_available": True
        }
        ]
    },
    {
        "Physiotherapy": [
        {
            "id": 61,
            "start_time": "2024-12-16T08:00:00",
            "end_time": "2024-12-16T08:45:00",
            "is_available": True
        },
        {
            "id": 62,
            "start_time": "2024-12-16T08:45:00",
            "end_time": "2024-12-16T09:30:00",
            "is_available": True
        },
        {
            "id": 63,
            "start_time": "2024-12-16T09:30:00",
            "end_time": "2024-12-16T10:15:00",
            "is_available": True
        },
        {
            "id": 64,
            "start_time": "2024-12-16T10:15:00",
            "end_time": "2024-12-16T11:00:00",
            "is_available": True
        },
        {
            "id": 65,
            "start_time": "2024-12-16T11:00:00",
            "end_time": "2024-12-16T11:45:00",
            "is_available": True
        },
        {
            "id": 66,
            "start_time": "2024-12-16T11:45:00",
            "end_time": "2024-12-16T12:30:00",
            "is_available": True
        },
        {
            "id": 67,
            "start_time": "2024-12-16T12:30:00",
            "end_time": "2024-12-16T13:15:00",
            "is_available": True
        },
        {
            "id": 68,
            "start_time": "2024-12-16T13:15:00",
            "end_time": "2024-12-16T14:00:00",
            "is_available": True
        },
        {
            "id": 69,
            "start_time": "2024-12-16T14:00:00",
            "end_time": "2024-12-16T14:45:00",
            "is_available": True
        },
        {
            "id": 70,
            "start_time": "2024-12-16T14:45:00",
            "end_time": "2024-12-16T15:30:00",
            "is_available": True
        }
        ]
    },
    {
        "Haircut": [
        {
            "id": 71,
            "start_time": "2024-12-17T08:00:00",
            "end_time": "2024-12-17T08:30:00",
            "is_available": True
        },
        {
            "id": 72,
            "start_time": "2024-12-17T08:30:00",
            "end_time": "2024-12-17T09:00:00",
            "is_available": True
        },
        {
            "id": 73,
            "start_time": "2024-12-17T09:00:00",
            "end_time": "2024-12-17T09:30:00",
            "is_available": True
        },
        {
            "id": 74,
            "start_time": "2024-12-17T09:30:00",
            "end_time": "2024-12-17T10:00:00",
            "is_available": True
        },
        {
            "id": 75,
            "start_time": "2024-12-17T10:00:00",
            "end_time": "2024-12-17T10:30:00",
            "is_available": True
        },
        {
            "id": 76,
            "start_time": "2024-12-17T10:30:00",
            "end_time": "2024-12-17T11:00:00",
            "is_available": True
        },
        {
            "id": 77,
            "start_time": "2024-12-17T11:00:00",
            "end_time": "2024-12-17T11:30:00",
            "is_available": True
        },
        {
            "id": 78,
            "start_time": "2024-12-17T11:30:00",
            "end_time": "2024-12-17T12:00:00",
            "is_available": True
        },
        {
            "id": 79,
            "start_time": "2024-12-17T12:00:00",
            "end_time": "2024-12-17T12:30:00",
            "is_available": True
        },
        {
            "id": 80,
            "start_time": "2024-12-17T12:30:00",
            "end_time": "2024-12-17T13:00:00",
            "is_available": True
        }
        ]
    },
    {
        "Spa Therapy": [
        {
            "id": 81,
            "start_time": "2024-12-18T08:00:00",
            "end_time": "2024-12-18T09:30:00",
            "is_available": True
        },
        {
            "id": 82,
            "start_time": "2024-12-18T09:30:00",
            "end_time": "2024-12-18T11:00:00",
            "is_available": True
        },
        {
            "id": 83,
            "start_time": "2024-12-18T11:00:00",
            "end_time": "2024-12-18T12:30:00",
            "is_available": True
        },
        {
            "id": 84,
            "start_time": "2024-12-18T12:30:00",
            "end_time": "2024-12-18T14:00:00",
            "is_available": True
        },
        {
            "id": 85,
            "start_time": "2024-12-18T14:00:00",
            "end_time": "2024-12-18T15:30:00",
            "is_available": True
        },
        {
            "id": 86,
            "start_time": "2024-12-18T15:30:00",
            "end_time": "2024-12-18T17:00:00",
            "is_available": True
        },
        {
            "id": 87,
            "start_time": "2024-12-18T17:00:00",
            "end_time": "2024-12-18T18:30:00",
            "is_available": True
        },
        {
            "id": 88,
            "start_time": "2024-12-18T18:30:00",
            "end_time": "2024-12-18T20:00:00",
            "is_available": True
        },
        {
            "id": 89,
            "start_time": "2024-12-18T20:00:00",
            "end_time": "2024-12-18T21:30:00",
            "is_available": True
        },
        {
            "id": 90,
            "start_time": "2024-12-18T21:30:00",
            "end_time": "2024-12-18T23:00:00",
            "is_available": True
        }
        ]
    },
    {
        "Bridal Makeup": [
        {
            "id": 91,
            "start_time": "2024-12-19T08:00:00",
            "end_time": "2024-12-19T10:00:00",
            "is_available": True
        },
        {
            "id": 92,
            "start_time": "2024-12-19T10:00:00",
            "end_time": "2024-12-19T12:00:00",
            "is_available": True
        },
        {
            "id": 93,
            "start_time": "2024-12-19T12:00:00",
            "end_time": "2024-12-19T14:00:00",
            "is_available": True
        },
        {
            "id": 94,
            "start_time": "2024-12-19T14:00:00",
            "end_time": "2024-12-19T16:00:00",
            "is_available": True
        },
        {
            "id": 95,
            "start_time": "2024-12-19T16:00:00",
            "end_time": "2024-12-19T18:00:00",
            "is_available": True
        },
        {
            "id": 96,
            "start_time": "2024-12-19T18:00:00",
            "end_time": "2024-12-19T20:00:00",
            "is_available": True
        },
        {
            "id": 97,
            "start_time": "2024-12-19T20:00:00",
            "end_time": "2024-12-19T22:00:00",
            "is_available": True
        },
        {
            "id": 98,
            "start_time": "2024-12-19T22:00:00",
            "end_time": "2024-12-20T00:00:00",
            "is_available": True
        },
        {
            "id": 99,
            "start_time": "2024-12-20T00:00:00",
            "end_time": "2024-12-20T02:00:00",
            "is_available": True
        },
        {
            "id": 100,
            "start_time": "2024-12-20T02:00:00",
            "end_time": "2024-12-20T04:00:00",
            "is_available": True
        }
        ]
    },
    {
        "DJ Service": [
        {
            "id": 101,
            "start_time": "2024-12-20T08:00:00",
            "end_time": "2024-12-20T12:00:00",
            "is_available": True
        },
        {
            "id": 102,
            "start_time": "2024-12-20T12:00:00",
            "end_time": "2024-12-20T16:00:00",
            "is_available": True
        },
        {
            "id": 103,
            "start_time": "2024-12-20T16:00:00",
            "end_time": "2024-12-20T20:00:00",
            "is_available": True
        },
        {
            "id": 104,
            "start_time": "2024-12-20T20:00:00",
            "end_time": "2024-12-20T24:00:00",
            "is_available": True
        },
        {
            "id": 105,
            "start_time": "2024-12-20T24:00:00",
            "end_time": "2024-12-21T04:00:00",
            "is_available": True
        },
        {
            "id": 106,
            "start_time": "2024-12-21T04:00:00",
            "end_time": "2024-12-21T08:00:00",
            "is_available": True
        },
        {
            "id": 107,
            "start_time": "2024-12-21T08:00:00",
            "end_time": "2024-12-21T12:00:00",
            "is_available": True
        },
        {
            "id": 108,
            "start_time": "2024-12-21T12:00:00",
            "end_time": "2024-12-21T16:00:00",
            "is_available": True
        },
        {
            "id": 109,
            "start_time": "2024-12-21T16:00:00",
            "end_time": "2024-12-21T20:00:00",
            "is_available": True
        },
        {
            "id": 110,
            "start_time": "2024-12-21T20:00:00",
            "end_time": "2024-12-21T24:00:00",
            "is_available": True
        }
        ]
    },
    {
        "Catering": [
        {
            "id": 111,
            "start_time": "2024-12-22T08:00:00",
            "end_time": "2024-12-22T14:00:00",
            "is_available": True
        },
        {
            "id": 112,
            "start_time": "2024-12-22T14:00:00",
            "end_time": "2024-12-22T20:00:00",
            "is_available": True
        },
        {
            "id": 113,
            "start_time": "2024-12-22T20:00:00",
            "end_time": "2024-12-23T02:00:00",
            "is_available": True
        },
        {
            "id": 114,
            "start_time": "2024-12-23T02:00:00",
            "end_time": "2024-12-23T08:00:00",
            "is_available": True
        },
        {
            "id": 115,
            "start_time": "2024-12-23T08:00:00",
            "end_time": "2024-12-23T14:00:00",
            "is_available": True
        },
        {
            "id": 116,
            "start_time": "2024-12-23T14:00:00",
            "end_time": "2024-12-23T20:00:00",
            "is_available": True
        },
        {
            "id": 117,
            "start_time": "2024-12-23T20:00:00",
            "end_time": "2024-12-24T02:00:00",
            "is_available": True
        },
        {
            "id": 118,
            "start_time": "2024-12-24T02:00:00",
            "end_time": "2024-12-24T08:00:00",
            "is_available": True
        },
        {
            "id": 119,
            "start_time": "2024-12-24T08:00:00",
            "end_time": "2024-12-24T14:00:00",
            "is_available": True
        },
        {
            "id": 120,
            "start_time": "2024-12-24T14:00:00",
            "end_time": "2024-12-24T20:00:00",
            "is_available": True
        }
        ]
    },
    {
        "Photography": [
        {
            "id": 121,
            "start_time": "2024-12-25T08:00:00",
            "end_time": "2024-12-25T10:00:00",
            "is_available": True
        },
        {
            "id": 122,
            "start_time": "2024-12-25T10:00:00",
            "end_time": "2024-12-25T12:00:00",
            "is_available": True
        },
        {
            "id": 123,
            "start_time": "2024-12-25T12:00:00",
            "end_time": "2024-12-25T14:00:00",
            "is_available": True
        },
        {
            "id": 124,
            "start_time": "2024-12-25T14:00:00",
            "end_time": "2024-12-25T16:00:00",
            "is_available": True
        },
        {
            "id": 125,
            "start_time": "2024-12-25T16:00:00",
            "end_time": "2024-12-25T18:00:00",
            "is_available": True
        },
        {
            "id": 126,
            "start_time": "2024-12-25T18:00:00",
            "end_time": "2024-12-25T20:00:00",
            "is_available": True
        },
        {
            "id": 127,
            "start_time": "2024-12-25T20:00:00",
            "end_time": "2024-12-25T22:00:00",
            "is_available": True
        },
        {
            "id": 128,
            "start_time": "2024-12-25T22:00:00",
            "end_time": "2024-12-26T00:00:00",
            "is_available": True
        },
        {
            "id": 129,
            "start_time": "2024-12-26T00:00:00",
            "end_time": "2024-12-26T02:00:00",
            "is_available": True
        },
        {
            "id": 130,
            "start_time": "2024-12-26T02:00:00",
            "end_time": "2024-12-26T04:00:00",
            "is_available": True
        }
        ]
    }
    ]
    
    for service in slots1:
        for service_name, slots in service.items():
            service = SlotifyService.objects.filter(name=service_name).first()
            slot = SlotifyServiceSlot.objects.filter(service=service)
            if slot.count() == 0: 
                for slot in slots:
                    SlotifyServiceSlot.objects.create(
                        service=service,
                        start_time=datetime.fromisoformat(slot["start_time"]),
                        end_time=datetime.fromisoformat(slot["end_time"]),
                        is_available=slot["is_available"]
                    )  
    
    
        
    