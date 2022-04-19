from app.models import db, Listing

def seed_listings():
    one = Listing(
        owner_id=1,
        title="Sweet beach house on the beach!",
        bed_number=4,
        bath_number=2,
        bedroom_number=4,
        maximum_guests=8,
        latitude=39.9124281,
        longitude=-74.07781299999999,
        city="Seaside Park",
        price=350,
        address="10-Ocean Avenue-08752",
        description="A nice get away along the New Jersey shoreline. Come spend a weekend away from the kids and learn how to live your life a little hehe xD. Equipped with all the necessities for a getaway that you'll be bragging about until you croak and die LOL. Seriously come by.",
        wifi_avail=True,
        tv_avail=True,
        kitchen_avail=True,
        ac_avail=False,
        washer_avail=False,
        dryer_avail=False,
        hair_dryer_avail=True,
        parking_avail=True,
        fridge_avail=True,
        bbq_avail=True,
        stove_avail=True,
        pool_avail=True,
        check_in="19:32",
        check_out="19:32",
        room_type_id=2,
    )
    two = Listing(
        owner_id=2,
        title="Recluse Cabin Nature Lover's Getaway",
        bed_number=3,
        bath_number=1,
        bedroom_number=3,
        maximum_guests=5,
        latitude=47.0500816,
        longitude=-96.936251,
        city="Argusville",
        price=250,
        address="101-Aldrich Avenue-58005",
        description="A homely cabin deep in the woods for you to come relax and unwind. Be surrounded by nature and achieve the calm you've been looking for in your busy life. Nearby lakes will offer you plenty to do in the summer-time while beautiful snowfall will keep you in awe come winter. Pets allowed.",
        wifi_avail=True,
        tv_avail=True,
        kitchen_avail=True,
        ac_avail=False,
        washer_avail=False,
        dryer_avail=False,
        hair_dryer_avail=False,
        parking_avail=True,
        fridge_avail=True,
        bbq_avail=True,
        stove_avail=True,
        pool_avail=False,
        check_in="10:00",
        check_out="10:00",
        room_type_id=3,
    )
    three = Listing(
        owner_id=3,
        title="Normal House in Denver",
        bed_number=4,
        bath_number=2,
        bedroom_number=4,
        maximum_guests=8,
        latitude=39.6516459,
        longitude=-105.0983282,
        city="Denver",
        price=300,
        address="9025-West Jefferson Avenue-80235",
        description="House in Denver for you to come be in Denver in. Ever been to Denver? No? Perfect come give me money to stay at my house. Is it clean? Probably. Take a chance at life come by haha.",
        wifi_avail=True,
        tv_avail=True,
        kitchen_avail=True,
        ac_avail=False,
        washer_avail=True,
        dryer_avail=True,
        hair_dryer_avail=True,
        parking_avail=True,
        fridge_avail=True,
        bbq_avail=True,
        stove_avail=True,
        pool_avail=False,
        check_in="12:00",
        check_out="12:00",
        room_type_id=2,
    )
    four = Listing(
        owner_id=4,
        title="NYC Apartment",
        bed_number=1,
        bath_number=1,
        bedroom_number=1,
        maximum_guests=4,
        latitude=40.790264,
        longitude=-73.9525967,
        city="New York",
        price=1000,
        address="1468-Madison Avenue-10029",
        description="Think my price is expensive? Its New York buddy go buy yaself a bacon egg and cheese to rid the tears. You're not renting from me because you want to, you're doing it because you need to. Pay up or click away.",
        wifi_avail=True,
        tv_avail=True,
        kitchen_avail=True,
        ac_avail=False,
        washer_avail=False,
        dryer_avail=False,
        hair_dryer_avail=False,
        parking_avail=False,
        fridge_avail=True,
        bbq_avail=False,
        stove_avail=True,
        pool_avail=False,
        check_in="8:00",
        check_out="8:00",
        room_type_id=4,
    )
    five = Listing(
        owner_id=5,
        title="Suburban Retreat",
        bed_number=4,
        bath_number=2,
        bedroom_number=4,
        maximum_guests=10,
        latitude=40.9786338,
        longitude=-74.0236041,
        city="Emerson",
        price=150,
        address="24-Highland Avenue-07630",
        description="Ever wonder what it's like to be in suburbia? Wonder no more and come spend some time at my house while I am away in the Bahamas spending my rich person money. Line my pockets further by indulging in the finest amenities an upper middle class home can offer. Pets allowed.",
        wifi_avail=True,
        tv_avail=True,
        kitchen_avail=True,
        ac_avail=True,
        washer_avail=True,
        dryer_avail=True,
        hair_dryer_avail=True,
        parking_avail=False,
        fridge_avail=True,
        bbq_avail=True,
        stove_avail=True,
        pool_avail=True,
        check_in="8:00",
        check_out="8:00",
        room_type_id=3,
    )
    db.session.add(one)
    db.session.add(two)
    db.session.add(three)
    db.session.add(four)
    db.session.add(five)
    db.session.commit()

def undo_seed_listings():
    db.session.execute('TRUNCATE listings RESTART IDENTITY CASCADE;')
    db.session.commit()
