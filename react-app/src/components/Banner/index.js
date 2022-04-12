import Modal from 'react-modal';
import LoginForm from '../auth/LoginForm';
import SignUpForm from '../auth/SignUpForm';
import { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { logout } from '../../store/session';
import './style/banner.css';

export const Banner = () => {
    const [visible, setVisible] = useState(false);
    const [modalIsOpen, setIsOpen] = useState(false);
    const [form, setForm] = useState(null);
    const user = useSelector((state) => state.session.user);
    const dispatch = useDispatch();

    const openModal = () => {
        setIsOpen(true);
        return;
    }

    const closeModal = () => {
        setIsOpen(false);
        return
    }

    const loginModal = () => {
        openModal();
        setForm('login');
    }

    const signUpModal = () => {
        openModal();
        setForm('signup');
    }

    const onLogout = async (e) => {
        await dispatch(logout());
    };

    let links;
    if (user) {
        links = (
            <>
                <div>
                    <p className='popout-item'>Trips</p>
                </div>
                <div>
                    <p className='popout-item'>Wishlist</p>
                </div>
                <div style={{ borderTop: "1px solid #DEDEDE" }}>
                    <div>
                        <p className='popout-item'>Host your home</p>
                    </div>
                    {/* <div>
                        <p className='popout-item'>Account</p>
                    </div> */}
                </div>
                <div style={{ borderTop: "1px solid #DEDEDE" }}>
                    <div>
                        <p className='popout-item'>Help</p>
                    </div>
                    <div>
                        <p
                            className='popout-item'
                            onClick={onLogout}>Log out</p>
                    </div>
                </div>
            </>
        )
    } if (!user) {
        links = (
            <>
                <div>
                    <p
                        className='popout-item'
                        onClick={loginModal}>Log in</p>
                </div>
                <div>
                    <p
                        className='popout-item'
                        onClick={signUpModal}>Sign up</p>
                </div>
                <div style={{ borderTop: "1px solid #DEDEDE" }}>
                    <div>
                        <p className='popout-item'>Host your home</p>
                    </div>
                    <div>
                        <p className='popout-item'>Help</p>
                    </div>
                </div>
            </>
        )
    }

    return (
        <div className="banner-container">
            <div className="banner-logo-container">
                <div>
                    <img
                        style={{ height: "32px", width: "20px" }}
                        src={require("./style/images/wanderer-logo.png").default} alt="logo"></img>
                </div>
                <div className='banner-logo-text-container'>
                    <p className='banner-logo-text'>wanderer</p>
                </div>
            </div>
            <div>
                <input
                    placeholder='Start your search'
                    style={{ width: "500px" }}
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
                            style={{ height: "20px", marginRight: "13px" }}
                            src={require('./style/images/three-lines.png').default} alt="threelines"></img>
                    </div>
                    <div>
                        <img src={require('./style/images/user-image.png').default} alt="userpic"></img>
                    </div>
                </div>
                <div className={visible ? 'user-interface-popout font' : 'hidden'}>
                    {links}
                </div>
            </div>
            <Modal
                className='form-modal'
                ariaHideApp={false}
                isOpen={modalIsOpen}
                onRequestClose={closeModal}
            >
                <div>
                    <div>x</div>
                    <p>Log in or Sign Up</p>
                </div>
                <div>
                    <p>Welcome to Wanderer</p>
                </div>
                {form === 'login' ? <LoginForm setIsOpen={setIsOpen} /> : form === 'signup' ? <SignUpForm /> : null}
            </Modal>
        </div>
    )
}

export default Banner;
