import { useState } from 'react';
import About from './About';
import Location from './Location';
import Amenities from './Amenities';
import Images from './Images';
import './style/listing-navbar.css';

const ListingNavBar = () => {

    const [active, setActive] = useState('About');
    const [title, setTitle] = useState("");
    const [beds, setBeds] = useState("");
    const [baths, setBaths] = useState("");
    const [bedrooms, setBedrooms] = useState("");
    const [guests, setGuests] = useState("");
    const [price, setPrice] = useState("");
    const [description, setDescription] = useState("");
    const [checkIn, setCheckIn] = useState("");
    const [checkOut, setCheckOut] = useState("");
    const [type, setType] = useState("");

    const [lat, setLat] = useState(null);
    const [long, setLong] = useState(null);
    const [city, setCity] = useState(null);
    const [address, setAddress] = useState(null);

    const [wifi, setWifi] = useState(false);
    const [tv, setTv] = useState(false);
    const [kitchen, setKitchen] = useState(false);
    const [ac, setAc] = useState(false);
    const [pool, setPool] = useState(false);
    const [washer, setWasher] = useState(false);
    const [dryer, setDryer] = useState(false);
    const [hairDryer, setHairDryer] = useState(false);
    const [parking, setParking] = useState(false);
    const [fridge, setFridge] = useState(false);
    const [bbq, setBbq] = useState(false);
    const [stove, setStove] = useState(false);

    const amenitiesFuncs = {
        wifi, setWifi,
        tv, setTv,
        kitchen, setKitchen,
        ac, setAc,
        pool, setPool,
        washer, setWasher,
        dryer, setDryer,
        hairDryer, setHairDryer,
        parking, setParking,
        fridge, setFridge,
        bbq, setBbq,
        stove, setStove
    }

    const locationFuncs = {
        lat, setLat,
        long, setLong,
        city, setCity,
        address, setAddress
    }

    const aboutFuncs = {
        active, setActive,
        title, setTitle,
        beds, setBeds,
        baths, setBaths,
        bedrooms, setBedrooms,
        guests, setGuests,
        price, setPrice,
        description, setDescription,
        checkIn, setCheckIn,
        checkOut, setCheckOut,
        type, setType
    }

    return (
        <>
            <div className="link-container">
                <div className="links-list">
                    <div
                        className={active === 'About' ? 'listing-nav-button selected' : 'listing-nav-button'}
                        onClick={() => setActive('About')}>
                        About the property
                    </div>
                    <div
                        className={active === 'Location' ? 'listing-nav-button selected' : 'listing-nav-button'}
                        onClick={() => setActive('Location')}>
                        Location
                    </div>
                    <div
                        className={active === 'Amenities' ? 'listing-nav-button selected' : 'listing-nav-button'}
                        onClick={() => setActive('Amenities')}>
                        Amenities
                    </div>
                    <div
                        className={active === 'Images' ? 'listing-nav-button selected' : 'listing-nav-button'}
                        onClick={() => setActive('Images')}>
                        Images
                    </div>
                </div>
            </div>
            <div style={{marginLeft: "10%"}}>
                {active === "About" ?
                    <About aboutFuncs={aboutFuncs} /> :
                    active === "Location" ?
                        <Location locationFuncs={locationFuncs}/> :
                        active === "Amenities" ?
                            <Amenities amenitiesFuncs={amenitiesFuncs}/> :
                            active === "Images" ?
                                <Images /> : null}
            </div>
        </>
    )
};

export default ListingNavBar;
