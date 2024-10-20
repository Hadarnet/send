import { RouteProp } from '@react-navigation/native';
import { StackNavigationProp } from '@react-navigation/stack';


export type RootStackParamList = {
    Login:undefined;
    Signup: undefined;
    SplashScreen: undefined;
    OtpScreen: { phoneNumber: string };
    ProfileScreen: undefined;
    Home: undefined;
    Calls: undefined;
    DialerScreen: undefined;
    ActiveCall: undefined;
    ChatHistory: undefined;
    ChatInterface: { chatId: string }; // Example of passing params
    DetailedCallHistory: { userId: string };
    BalanceScreen: undefined;
    Settings: undefined;
    PaymentScreen: undefined;
    // Add other screens and their params here
  };
  


  export type OtpScreenNavigationProp = StackNavigationProp<RootStackParamList, 'OtpScreen'>;
export type OtpScreenRouteProp = RouteProp<RootStackParamList, 'OtpScreen'>;