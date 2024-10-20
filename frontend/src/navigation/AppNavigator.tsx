import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import { NavigationContainer } from '@react-navigation/native';

import { RootStackParamList } from './types';

// Import your screens

import SignupScreen from '../screens/SignUpScreen';
import HomeScreen from '../screens/HomeScreen';
import CallsScreen from '../screens/CallsScreen';
import ActiveCallScreen from '../screens/ActiveCallScreen';

import ChatInterfaceScreen from '../screens/ChatInterfaceScreen';
import DetailedCallHistoryScreen from '../screens/DetailedCallHistoryScreen';
import WalletScreen from '../screens/BalanceScreen';
import SettingsScreen from '../screens/SettingsScreen';
import SplashScreen from '../screens/SplashScreen';
import OtpScreen from '../screens/OtpScreen';
import ProfileScreen from '../screens/ProfileScreen';
import ContactsScreen from '../screens/Contacts';
import DialerScreen from '../screens/DialerScreen';
import BalanceScreen from '../screens/BalanceScreen';
import PaymentScreen from '../screens/PaymentScreen';


const Stack = createStackNavigator<RootStackParamList>();

const AppNavigator: React.FC = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="SplashScreen">
      <Stack.Screen 
          name="SplashScreen" 
          component={SplashScreen} 
          options={{ headerShown: false }} 
        />
        <Stack.Screen 
          name="Signup" 
          component={SignupScreen} 
          options={{ headerShown: false }} 
        />

        <Stack.Screen 
          name="OtpScreen" 
          component={OtpScreen} 
          options={{ headerShown: false }} 
        />

        <Stack.Screen 
          name="ProfileScreen" 
          component={ProfileScreen} 
          options={{ headerShown: false }} 
        />

        <Stack.Screen 
          name="Home" 
          component={HomeScreen} 
          options={{ headerShown: false }} 
        />
        <Stack.Screen 
          name="Calls" 
          component={CallsScreen} 
          options={{ headerShown: false }}  
        />
        <Stack.Screen 
          name="ActiveCall" 
          component={ActiveCallScreen} 
          options={{ headerShown: false }} 
        />
        <Stack.Screen 
          name="ChatHistory" 
          component={ContactsScreen} 
          options={{ headerShown: false }}  
        />
        <Stack.Screen 
          name="DialerScreen" 
          component={DialerScreen} 
          options={{ headerShown: false }}  
        />
        <Stack.Screen 
          name="ChatInterface" 
          component={ChatInterfaceScreen} 
          options={{ headerShown: false }}  
        />
        <Stack.Screen 
          name="DetailedCallHistory" 
          component={DetailedCallHistoryScreen} 
          options={{ headerShown: false }} 
        />
        <Stack.Screen 
          name="BalanceScreen" 
          component={BalanceScreen} 
          options={{ headerShown: false }} 
        />
        <Stack.Screen 
          name="Settings" 
          component={SettingsScreen} 
          options={{ headerShown: false }}  
        />
        <Stack.Screen 
          name="PaymentScreen" 
          component={PaymentScreen} 
          options={{ headerShown: false }}  
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default AppNavigator;
