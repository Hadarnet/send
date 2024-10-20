import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, StyleProp, ViewStyle, TextStyle } from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';

interface HeaderProps {
  title: string;
  leftIcon?: string;
  onLeftPress?: () => void;
  rightIcon?: string;
  onRightPress?: () => void;
  containerStyle?: StyleProp<ViewStyle>;
  titleStyle?: StyleProp<TextStyle>;
  iconButtonStyle?: StyleProp<ViewStyle>;
}

const Header: React.FC<HeaderProps> = ({
  title,
  leftIcon,
  onLeftPress,
  rightIcon,
  onRightPress,
  containerStyle,
  titleStyle,
  iconButtonStyle,
}) => {
  return (
    <View style={[styles.container, containerStyle]}>
      {leftIcon ? (
        <TouchableOpacity onPress={onLeftPress} style={[styles.iconButton, iconButtonStyle]} activeOpacity={0.7}>
          <Icon name={leftIcon} size={24} color="#fff" />
        </TouchableOpacity>
      ) : (
        <View style={styles.placeholder} />
      )}
      <Text style={[styles.title, titleStyle]}>{title}</Text>
      {rightIcon ? (
        <TouchableOpacity onPress={onRightPress} style={[styles.iconButton, iconButtonStyle]} activeOpacity={0.7}>
          <Icon name={rightIcon} size={24} color="#fff" />
        </TouchableOpacity>
      ) : (
        <View style={styles.placeholder} />
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    height: 60,
    backgroundColor: '#0f1828', // Dark background for the header
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 10,
    borderBottomWidth: 0.5,
    borderBottomColor: '#2E0854', // Border color matching the background
  },
  iconButton: {
    padding: 10,
  },
  placeholder: {
    width: 44, // To match icon button size
  },
  title: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '500', // Slightly less bold than 'bold'
    textAlign: 'center', // Centered title
  },
});

export default Header;
