import { GoogleMap, Marker } from '@react-google-maps/api';
import './style/maps.css';

const SearchMap = ({ lat, lng, style }) => {

    const center = {
        lat,
        lng
    }

    return (
        <>
                <GoogleMap mapTypeId='satellite' center={center} zoom={14} mapContainerStyle={style ? { height: "90vh" } : { width: '1000px', height: "500px" }}>
                    <Marker
                        // generates a blank icon
                        icon={"data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="}
                        label={
                            {
                                // TODO string interpolated nightly cost
                                text: `$54`,
                                className: 'marker-label'
                            }
                        }
                        position={center} />
                </GoogleMap>
        </>
    )
};

export default SearchMap;
