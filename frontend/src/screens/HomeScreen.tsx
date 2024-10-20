import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Icon from 'react-native-vector-icons/Ionicons';
import ContactsScreen from './Contacts';  // Import your contacts and other screens

import WebScreen from '../screens/ChatInterfaceScreen';
import SettingsScreen from '../screens/SettingsScreen';
import ChatsScreen from './Chats';
import ChatInterfaceScreen from '../screens/ChatInterfaceScreen';
import DialerScreen from './DialerScreen';
import BalanceScreen from './BalanceScreen';

const Tab = createBottomTabNavigator();

const HomeScreen = () => {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ color, size }) => {
          let iconName;

          if (route.name === 'Contacts') {
            iconName = 'people-outline';
          } else if (route.name === 'ChatInterface') {
            iconName = 'call-outline';
          } else if (route.name === 'Web') {
            iconName = 'globe-outline';
          } else if (route.name === 'Settings') {
            iconName = 'settings-outline';
          } else if (route.name === 'Chats') {
            iconName = 'chatbubble-outline';
          }

          return <Icon name={iconName} size={size} color={color} />;
        },
        tabBarActiveTintColor: '#FFFFFF',
        tabBarInactiveTintColor: '#9CA3AF',
        tabBarStyle: {
          backgroundColor: '#152033',
        },
        headerShown: false,
      })}
    >
      <Tab.Screen name="Contacts" component={ContactsScreen} />
      <Tab.Screen name="Chats" component={ChatsScreen} />
      <Tab.Screen name="ChatInterface" component={BalanceScreen} />
      <Tab.Screen name="Dialer" component={DialerScreen} />
      <Tab.Screen name="Settings" component={SettingsScreen} />
    </Tab.Navigator>
  );
};

export default HomeScreen;
