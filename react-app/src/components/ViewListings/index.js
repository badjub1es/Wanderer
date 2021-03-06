import { useDispatch, useSelector } from 'react-redux';
import { useEffect, useState } from 'react';
import { getAllListings } from '../../store/listings';
import ListingCard from './ListingCard';
import './style/view-listings.css';

const ViewListings = () => {
    const listings = useSelector((state) => Object.values(state.listings.listings))
    const dispatch = useDispatch();

    const [loaded, setLoaded] = useState(false);

    // token for pagination of listing results
    const [pagToken, setPagToken] = useState(0);

    // gets (15) listings, offset by current pagination (pag) token
    // pag token increments on each call of loadMoreListings
    useEffect(() => {
        dispatch(getAllListings(pagToken, 15))
            .then(() => {
                setLoaded(true);
                setPagToken((t) => t + 1);
            });
        // eslint-disable-next-line
    }, [dispatch]);

    const loadMoreListings = () => {
        dispatch(getAllListings(pagToken, 15))
                .then(() => setPagToken((t) => t + 1));
    };

    return (
        <>
            {loaded ? (
                <div
                    className='all-listings-container'>
                    {loaded && listings?.map((listing) => (
                        <div style={{ width: "300px", margin: "0px 40px 40px 40px" }}>
                            <ListingCard
                                key={listing?.id}
                                listing={listing} />
                        </div>
                    ))}
                </div>) : <img alt="loading" src={require('../LoadingModal/style/loader/Preloader_1.gif').default} />}
            <div
                className='load-listings'
                onClick={loadMoreListings}>
                    Load more listings
            </div>
        </>

    )
};

export default ViewListings;
