import React from 'react';
import {
  TouchableOpacity,
  Text,
  StyleSheet,
  ActivityIndicator,
  GestureResponderEvent,
  StyleProp,
  ViewStyle,
  TextStyle,
} from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';

interface CustomButtonProps {
  title: string;
  onPress: (event: GestureResponderEvent) => void;
  iconName?: string;
  iconPosition?: 'left' | 'right';
  disabled?: boolean;
  loading?: boolean;
  style?: StyleProp<ViewStyle>;
  textStyle?: StyleProp<TextStyle>;
}

const CustomButton: React.FC<CustomButtonProps> = ({
  title,
  onPress,
  iconName,
  iconPosition = 'left',
  disabled = false,
  loading = false,
  style,
  textStyle,
}) => {
  return (
    <TouchableOpacity
      style={[styles.button, style, disabled && styles.disabled]}
      onPress={onPress}
      disabled={disabled || loading}
      activeOpacity={0.7}
    >
      {loading ? (
        <ActivityIndicator color="#fff" />
      ) : (
        <>
          {iconName && iconPosition === 'left' && (
            <Icon name={iconName} size={20} color="#fff" style={styles.icon} />
          )}
          <Text style={[styles.text, textStyle]}>{title}</Text>
          {iconName && iconPosition === 'right' && (
            <Icon name={iconName} size={20} color="#fff" style={styles.icon} />
          )}
        </>
      )}
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  button: {
    flexDirection: 'row',
    backgroundColor: '#5A2A83',
    padding: 15,
    borderRadius: 10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  disabled: {
    backgroundColor: '#A28FCF',
  },
  text: {
    color: '#fff',
    fontSize: 16,
    marginHorizontal: 5,
  },
  icon: {
    marginHorizontal: 5,
  },
});

export default CustomButton;
