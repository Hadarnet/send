import React from 'react';
import { View, Text, StyleSheet, StyleProp, ViewStyle, TextStyle } from 'react-native';

interface WalletBalanceProps {
  currency: string;
  balance: number;
  dollarValue: number;
  containerStyle?: StyleProp<ViewStyle>;
  currencyStyle?: StyleProp<TextStyle>;
  balanceStyle?: StyleProp<TextStyle>;
  dollarValueStyle?: StyleProp<TextStyle>;
}

const WalletBalance: React.FC<WalletBalanceProps> = ({
  currency,
  balance,
  dollarValue,
  containerStyle,
  currencyStyle,
  balanceStyle,
  dollarValueStyle,
}) => {
  return (
    <View style={[styles.container, containerStyle]}>
      <Text style={[styles.currency, currencyStyle]}>{currency}</Text>
      <Text style={[styles.balance, balanceStyle]}>{balance}</Text>
      <Text style={[styles.dollarValue, dollarValueStyle]}>${dollarValue.toFixed(2)}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#3A0078',
    padding: 20,
    borderRadius: 10,
    alignItems: 'center',
    marginVertical: 10,
  },
  currency: {
    fontSize: 18,
    color: '#fff',
  },
  balance: {
    fontSize: 32,
    color: '#fff',
    fontWeight: 'bold',
    marginVertical: 5,
  },
  dollarValue: {
    fontSize: 16,
    color: '#ccc',
  },
});

export default WalletBalance;
