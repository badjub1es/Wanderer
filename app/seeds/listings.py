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
        state="New Jersey",
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
        state="North Dakota",
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
        state="Colorado",
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
        state="NY",
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
        state="New Jersey",
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
    six = Listing(
        owner_id=2,
        title="Easy going apartment in NYC.",
        bed_number=2,
        bath_number=1,
        bedroom_number=1,
        maximum_guests=4,
        latitude="40.7631466",
        longitude="-73.9622114",
        state="New York",
        city="NY",
        price=300,
        address="301-East 63rd Street-10065",
        description="Clean apartment for anyone trying to spend some time in the big apple.",
        wifi_avail=True,
        tv_avail=True,
        kitchen_avail=True,
        ac_avail=True,
        washer_avail=False,
        dryer_avail=False,
        hair_dryer_avail=True,
        parking_avail=False,
        fridge_avail=True,
        bbq_avail=False,
        stove_avail=True,
        pool_avail=False,
        check_in="10:00",
        check_out="10:00",
        room_type_id=4,
    )
    seven = Listing(
        owner_id=2,
        title="Slick apartment with all the bells and whistles.",
        bed_number=2,
        bath_number=1,
        bedroom_number=1,
        maximum_guests=5,
        latitude="40.7733706",
        longitude="-73.96255959999999",
        state="New York",
        city="NY",
        price=150,
        address="820-Park Avenue-10021",
        description="Come stay at a beautiful apartment that is sure to rock your socks.",
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
        check_in="10:00",
        check_out="10:00",
        room_type_id=4,
    )
    eight = Listing(
        owner_id=2,
        title="NYC apartment, chill vibes only.",
        bed_number=1,
        bath_number=1,
        bedroom_number=1,
        maximum_guests=2,
        latitude="40.7650253",
        longitude="-73.9676403",
        state="New York",
        city="NY",
        price=400,
        address="575-Park Avenue-10065",
        description="For chillers by chillers. If you are not a chiller then do not come by. Rad.",
        wifi_avail=False,
        tv_avail=False,
        kitchen_avail=True,
        ac_avail=True,
        washer_avail=True,
        dryer_avail=True,
        hair_dryer_avail=True,
        parking_avail=False,
        fridge_avail=False,
        bbq_avail=False,
        stove_avail=True,
        pool_avail=False,
        check_in="12:00",
        check_out="12:00",
        room_type_id=4,
    )
    nine = Listing(
        owner_id=2,
        title="NYC apartment, bad vibes only.",
        bed_number=1,
        bath_number=1,
        bedroom_number=1,
        maximum_guests=5,
        latitude="40.764050",
        longitude="-73.964336",
        state="New York",
        city="NY",
        price=500,
        address="205-East 63rd Street-10065",
        description="If you have bad vibes then isolate them here in my perfectly terrible listing. No pets.",
        wifi_avail=False,
        tv_avail=False,
        kitchen_avail=False,
        ac_avail=False,
        washer_avail=False,
        dryer_avail=False,
        hair_dryer_avail=True,
        parking_avail=False,
        fridge_avail=True,
        bbq_avail=True,
        stove_avail=True,
        pool_avail=True,
        check_in="5:00",
        check_out="5:00",
        room_type_id=4,
    )
    ten = Listing(
        owner_id=2,
        title="Simple stay in a loud place.",
        bed_number=2,
        bath_number=1,
        bedroom_number=2,
        maximum_guests=6,
        latitude="40.7784336",
        longitude="-73.9575946",
        state="New York",
        city="NY",
        price=500,
        address="108-East 84th Street-10028",
        description="Come stay at an expensive loud place! Sure to be memerable and if its not then that works too LOL.",
        wifi_avail=True,
        tv_avail=True,
        kitchen_avail=True,
        ac_avail=True,
        washer_avail=False,
        dryer_avail=False,
        hair_dryer_avail=True,
        parking_avail=False,
        fridge_avail=True,
        bbq_avail=False,
        stove_avail=True,
        pool_avail=False,
        check_in="9:00",
        check_out="9:00",
        room_type_id=4,
    )
    eleven = Listing(
        owner_id=2,
        title="Cozy apartment for cozy people vol. I.",
        bed_number=1,
        bath_number=1,
        bedroom_number=1,
        maximum_guests=2,
        latitude="40.7821817",
        longitude="-73.9466937",
        state="New York",
        city="NY",
        price=200,
        address="328-East 94th Street-10128",
        description="Its super cozy in here and you dont have to take my word for it! Well... I guess you have to take my word for it...",
        wifi_avail=True,
        tv_avail=True,
        kitchen_avail=True,
        ac_avail=True,
        washer_avail=False,
        dryer_avail=False,
        hair_dryer_avail=False,
        parking_avail=False,
        fridge_avail=True,
        bbq_avail=False,
        stove_avail=True,
        pool_avail=False,
        check_in="10:00",
        check_out="10:00",
        room_type_id=4,
    )
    twelve = Listing(
        owner_id=2,
        title="Do not stay in this apartment.",
        bed_number=1,
        bath_number=1,
        bedroom_number=1,
        maximum_guests=1,
        latitude="40.7834299",
        longitude="-73.95634849999999",
        state="New York",
        city="NY",
        price=50,
        address="51-East 90th Street-10128",
        description="I promise it is too good to be true. DO NOT STAY HERE!!",
        wifi_avail=False,
        tv_avail=False,
        kitchen_avail=False,
        ac_avail=False,
        washer_avail=True,
        dryer_avail=True,
        hair_dryer_avail=True,
        parking_avail=False,
        fridge_avail=True,
        bbq_avail=True,
        stove_avail=False,
        pool_avail=False,
        check_in="12:00",
        check_out="12:00",
        room_type_id=4,
    )
    thirteen = Listing(
        owner_id=2,
        title="Cozy apartment for cozy people, vol. II.",
        bed_number=1,
        bath_number=1,
        bedroom_number=1,
        maximum_guests=2,
        latitude="40.76366319999999",
        longitude="-73.9655082",
        state="New York",
        city="NY",
        price=200,
        address="175-East 62nd Street-10065",
        description="You've heard of cozy apartment for cozy people, vol. I, and now we bring you vol. II!!!!! Pets allowed.",
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
        check_in="9:00",
        check_out="9:00",
        room_type_id=4,
    )
    fourteen = Listing(
        owner_id=2,
        title="The best apartment ever trust me, I'm a doctor.",
        bed_number=4,
        bath_number=2,
        bedroom_number=5,
        maximum_guests=15,
        latitude="40.7720984",
        longitude="-73.9618424",
        state="New York",
        city="NY",
        price=700,
        address="125-East 74th Street-10021",
        description="This has to be hands down the best apartment to ever exist. My mom says so.",
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
        check_in="10:00",
        check_out="10:00",
        room_type_id=4,
    )
    den_2 = Listing(
        owner_id=3,
        title="Delectable apartment in Denver.",
        bed_number=2,
        bath_number=1,
        bedroom_number=2,
        maximum_guests=5,
        latitude="39.7708456",
        longitude="-105.0437485",
        state="Colorado",
        city="Denver",
        price=250,
        address="4390-West 39th Avenue-80212",
        description="A snazzy apartment in Denver. Come by and enjoy nature or don't, doesn't matter to me!",
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
        check_in="10:00",
        check_out="10:00",
        room_type_id=4,
    )
    den_3 = Listing(
        owner_id=3,
        title="My house is now your house.",
        bed_number=3,
        bath_number=2,
        bedroom_number=3,
        maximum_guests=8,
        latitude="39.7391781",
        longitude="-104.959078",
        state="Colorado",
        city="Denver",
        price=400,
        address="1441-Josephine Street-80206",
        description="A nicely lived in home for you and your friends to come have a time in. Have a time indeed.",
        wifi_avail=True,
        tv_avail=True,
        kitchen_avail=True,
        ac_avail=True,
        washer_avail=True,
        dryer_avail=True,
        hair_dryer_avail=True,
        parking_avail=False,
        fridge_avail=True,
        bbq_avail=False,
        stove_avail=False,
        pool_avail=False,
        check_in="12:00",
        check_out="12:00",
        room_type_id=3,
    )
    den_4 = Listing(
        owner_id=3,
        title="Mi casa es tu casa! In Denver.",
        bed_number=3,
        bath_number=1,
        bedroom_number=2,
        maximum_guests=6,
        latitude="39.7393772",
        longitude="-104.9767402",
        state="Colorado",
        city="Denver",
        price=200,
        address="1449-Emerson Street-80218",
        description="Some way or another you'll end up in Denver. When that time comes, come to my house lol.",
        wifi_avail=True,
        tv_avail=True,
        kitchen_avail=True,
        ac_avail=True,
        washer_avail=True,
        dryer_avail=True,
        hair_dryer_avail=False,
        parking_avail=False,
        fridge_avail=True,
        bbq_avail=True,
        stove_avail=True,
        pool_avail=False,
        check_in="10:00",
        check_out="10:00",
        room_type_id=3,
    )
    den_5 = Listing(
        owner_id=3,
        title="Denver apartment ready for living in.",
        bed_number=2,
        bath_number=1,
        bedroom_number=2,
        maximum_guests=2,
        latitude="39.7306786",
        longitude="-104.9324516",
        state="Colorado",
        city="Denver",
        price=400,
        address="880-Dexter Street-80220",
        description="Apartment ready for living in. Apartment used to be not ready to live in but now it is.",
        wifi_avail=True,
        tv_avail=True,
        kitchen_avail=True,
        ac_avail=True,
        washer_avail=True,
        dryer_avail=True,
        hair_dryer_avail=True,
        parking_avail=False,
        fridge_avail=True,
        bbq_avail=False,
        stove_avail=False,
        pool_avail=False,
        check_in="10:00",
        check_out="10:00",
        room_type_id=4,
    )
    den_6 = Listing(
        owner_id=3,
        title="It is a house. It is in Denver!",
        bed_number=2,
        bath_number=2,
        bedroom_number=2,
        maximum_guests=6,
        latitude="39.6771402",
        longitude="-104.9838147",
        state="Colorado",
        city="Denver",
        price=300,
        address="2174-South Grant Street-80210",
        description="This house is in Denver. This house is very nice. I like this house. Rent my house thanks :).",
        wifi_avail=True,
        tv_avail=True,
        kitchen_avail=False,
        ac_avail=True,
        washer_avail=True,
        dryer_avail=True,
        hair_dryer_avail=False,
        parking_avail=False,
        fridge_avail=True,
        bbq_avail=True,
        stove_avail=False,
        pool_avail=False,
        check_in="10:00",
        check_out="10:00",
        room_type_id=3,
    )
    den_7 = Listing(
        owner_id=3,
        title="An apartment for you, by me!",
        bed_number=2,
        bath_number=1,
        bedroom_number=1,
        maximum_guests=4,
        latitude="39.6881562",
        longitude="-104.8803524",
        state="Colorado",
        city="Denver",
        price=150,
        address="9300-East Florida Avenue-80247",
        description="It might be small but that does not mean anything really. You are also wrong. Please rent here.",
        wifi_avail=False,
        tv_avail=False,
        kitchen_avail=False,
        ac_avail=False,
        washer_avail=True,
        dryer_avail=True,
        hair_dryer_avail=True,
        parking_avail=False,
        fridge_avail=True,
        bbq_avail=True,
        stove_avail=True,
        pool_avail=True,
        check_in="10:00",
        check_out="10:00",
        room_type_id=3,
    )
    den_8 = Listing(
        owner_id=3,
        title="Cozy spot for you folks.",
        bed_number=2,
        bath_number=2,
        bedroom_number=2,
        maximum_guests=4,
        latitude="39.7327423",
        longitude="-104.9851155",
        state="Colorado",
        city="Denver",
        price=350,
        address="1035-Sherman Street-80203",
        description="When in Rome, do as the Denver people do. You are now in Rome so this is the place to be get it while its hot hot hot!",
        wifi_avail=True,
        tv_avail=True,
        kitchen_avail=True,
        ac_avail=True,
        washer_avail=True,
        dryer_avail=True,
        hair_dryer_avail=False,
        parking_avail=False,
        fridge_avail=False,
        bbq_avail=True,
        stove_avail=True,
        pool_avail=False,
        check_in="10:00",
        check_out="10:00",
        room_type_id=4,
    )
    den_9 = Listing(
        owner_id=3,
        title="Spiffy apartment that will totally knock your socks clean off your feet.",
        bed_number=2,
        bath_number=1,
        bedroom_number=2,
        maximum_guests=6,
        latitude="39.7437656",
        longitude="-104.9900254",
        state="Colorado",
        city="Denver",
        price=500,
        address="1600-Glenarm Place-80202",
        description="Is the price steep? Possibly, depending on what kind of steep you are talking. Call me to discuss payment plans.",
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
        check_in="09:00",
        check_out="09:00",
        room_type_id=4,
    )
    den_10 = Listing(
        owner_id=3,
        title="Grandma's House",
        bed_number=2,
        bath_number=1,
        bedroom_number=2,
        maximum_guests=10,
        latitude="39.7380302",
        longitude="-104.9681142",
        state="Colorado",
        city="Denver",
        price=50,
        address="1364-Franklin Street-8021",
        description="Grandma is lonely. Please come spend time with Grandma, Grandma misses you ;[.",
        wifi_avail=False,
        tv_avail=False,
        kitchen_avail=True,
        ac_avail=True,
        washer_avail=True,
        dryer_avail=True,
        hair_dryer_avail=True,
        parking_avail=False,
        fridge_avail=True,
        bbq_avail=True,
        stove_avail=True,
        pool_avail=False,
        check_in="05:00",
        check_out="05:00",
        room_type_id=4,
    )
    db.session.add(one)
    db.session.add(two)
    db.session.add(three)
    db.session.add(four)
    db.session.add(five)
    db.session.add(six)
    db.session.add(seven)
    db.session.add(eight)
    db.session.add(nine)
    db.session.add(ten)
    db.session.add(eleven)
    db.session.add(twelve)
    db.session.add(thirteen)
    db.session.add(fourteen)
    db.session.add(den_2) # 15
    db.session.add(den_3) # 16
    db.session.add(den_4) # 17
    db.session.add(den_5) # 18
    db.session.add(den_6) # 19
    db.session.add(den_7) # 20
    db.session.add(den_8) # 21
    db.session.add(den_9) # 22
    db.session.add(den_10) # 23
    db.session.commit()

def undo_seed_listings():
    db.session.execute('TRUNCATE listings RESTART IDENTITY CASCADE;')
    db.session.commit()
