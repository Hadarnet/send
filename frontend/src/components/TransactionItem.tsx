import React from 'react';
import { View, Text, StyleSheet, StyleProp, ViewStyle, TextStyle } from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';

interface TransactionItemProps {
  type: 'send' | 'receive' | 'withdraw';
  amount: number;
  currency: string;
  date: string;
  containerStyle?: StyleProp<ViewStyle>;
  amountStyle?: StyleProp<TextStyle>;
  dateStyle?: StyleProp<TextStyle>;
}

const TransactionItem: React.FC<TransactionItemProps> = ({
  type,
  amount,
  currency,
  date,
  containerStyle,
  amountStyle,
  dateStyle,
}) => {
  const getIconName = (): string => {
    switch (type) {
      case 'send':
        return 'arrow-up';
      case 'receive':
        return 'arrow-down';
      case 'withdraw':
        return 'swap-horizontal';
      default:
        return 'swap-horizontal';
    }
  };

  const iconName = getIconName();
  const isSend = type === 'send';

  return (
    <View style={[styles.container, containerStyle]}>
      <Icon name={iconName} size={24} color="#5A2A83" />
      <View style={styles.details}>
        <Text style={[styles.amount, amountStyle]}>
          {isSend ? '-' : '+'}
          {amount} {currency}
        </Text>
        <Text style={[styles.date, dateStyle]}>{date}</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    padding: 15,
    backgroundColor: '#3A0078',
    borderRadius: 8,
    alignItems: 'center',
    marginVertical: 5,
  },
  details: {
    marginLeft: 15,
  },
  amount: {
    fontSize: 16,
    color: '#fff',
    fontWeight: 'bold',
  },
  date: {
    fontSize: 12,
    color: '#ccc',
    marginTop: 2,
  },
});

export default TransactionItem;
