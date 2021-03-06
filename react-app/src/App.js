import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { authenticate } from './store/session';
import { Redirect } from 'react-router-dom';
import ProtectedRoute from './components/auth/ProtectedRoute';
import Banner from './components/Banner';
import ListingProfile from './components/ListingProfile';
import ListingForm from './components/ListingForm';
import MyTrips from './components/MyTrips';
import MyListings from './components/MyListings';
import TripPage from './components/TripPage';
import HomePage from './components/HomePage';
import ViewListings from './components/ViewListings';
import SplashPage from './components/SplashPage';
import SearchResult from './components/SearchResult';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <Banner />
      <Switch>
        <Route path='/listings/:listingId(\d+)' exact={true}>
         <ListingProfile />
        </Route>
        <Route path='/view-listings' exact={true}>
          <ViewListings />
        </Route>
        <ProtectedRoute path='/my-listings' exact={true} >
          <MyListings />
        </ProtectedRoute>
        <ProtectedRoute path='/my-trips' exact={true} >
          <MyTrips />
        </ProtectedRoute>
        <ProtectedRoute path='/trips/:reservationId(\d+)' exact={true} >
          <TripPage />
        </ProtectedRoute>
        <ProtectedRoute path='/create-listing' exact={true} >
          <ListingForm />
        </ProtectedRoute>
        <Route path='/s/:searchTerm/:lat/:lng' exact={true}>
          <SearchResult />
        </Route>
        <Route path='/' exact={true}>
          <SplashPage />
        </Route>
        <Route path='/home' exact={true} >
          <HomePage />
        </Route>
        <Route path='/'>
          <Redirect to="/home" />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
