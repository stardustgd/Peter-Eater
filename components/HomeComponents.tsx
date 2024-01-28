import { Button, Text } from 'react-native'

const HomeScreen = ({ navigation }) => {
    return (
        <Button
            title="Welcome"
            onPress={() =>
                navigation.navigate('Menu', { name: 'Jane' })
            }
        />
    );
};
const ProfileScreen = ({ navigation, route }) => {
    return <Text>This is {route.params.name}'s profile</Text>;
};

export default HomeScreen;
