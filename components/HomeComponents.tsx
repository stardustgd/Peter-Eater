import { Button, Text } from 'react-native'

const HomeScreen = ({ navigation }: {navigation: any}) => {
    return (
        <Button
            title="Welcome"
            onPress={() =>
                navigation.navigate('Menu', { name: 'Jane' })
            }
        />
    );
};
const ProfileScreen = ({ navigation, route }: {navigation: any, route: any}) => {
    return <Text>This is {route.params.name}'s profile</Text>;
};

export default HomeScreen;
