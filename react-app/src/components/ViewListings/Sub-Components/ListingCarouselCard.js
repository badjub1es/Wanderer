import { useHistory } from "react-router-dom";

const ListingCarouselCard = ({img}) => {
    const history = useHistory();
    const url = img.url?.split('=index?')[0];

    return (
        <div
            style={{cursor: "pointer"}}
            onClick={() => history.push(`/listings/${img?.listing_id}`)}>
            <img
                alt="listing"
                style={{
                    height: "300px",
                    objectFit: "cover",
                    borderRadius: "15px"
                }}
                src={url}></img>
        </div>
    )
};

export default ListingCarouselCard;
