import { useState } from 'react';
import './style/banner.css';

export const Banner = () => {
    const [visible, setVisible] = useState(false);

    return (
        <div className="banner-container">
            <div className="banner-logo-container">
                <div>
                <img
                    style={{height: "32px", width: "20px"}}
                    src={require("./style/images/wanderer-logo.png").default} alt=""></img>
                </div>
                <div className='banner-logo-text-container'>
                    <p className='banner-logo-text'>wanderer</p>
                </div>
            </div>
            <div>
                <input
                    placeholder='Start your search'
                    style={{width: "500px"}}
                    className='banner-search-bar'
                    type="text">
                </input>
            </div>

            <div
                className='banner-user-interface'
                onClick={() => setVisible(!visible)}>
                <div className='banner-user-interface-container'>
                    <div>
                        <img
                            style={{height: "20px", marginRight: "13px"}}
                            src={require('./style/images/three-lines.png').default}></img>
                    </div>
                    <div>
                        <img src={require('./style/images/user-image.png').default}></img>
                    </div>
                </div>
                    <div className={visible ? 'user-interface-popout font' : 'hidden'}>
                        <div>
                            <p className='popout-item'>Log in</p>
                        </div>
                        <div>
                            <p className='popout-item'>Sign up</p>
                        </div>
                        <div style={{borderTop: "1px solid #DEDEDE"}}>
                            <div>
                                <p className='popout-item'>Host your home</p>
                            </div>
                            <div>
                                <p className='popout-item'>Help</p>
                            </div>
                        </div>
                    </div>
            </div>
        </div>
    )
}

export default Banner;
