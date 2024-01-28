import { useEffect, useState } from 'react'
import {
    Dimensions,
    FlatList,
    Text,
    View,
    ScrollView,
    StyleSheet,
    StatusBar,
    TouchableOpacity
} from 'react-native'

import { Button } from 'react-native'

const ReviewScreen = ({ navigation }: {navigation: any}) => {
    return (
        <Text>Review Screen</Text>
    );
};
const ProfileScreen = ({ navigation, route }: {navigation: any, route: any}) => {
    return <Text>This is {route.params.name}'s profile</Text>;
};

export default ReviewScreen;


// const styles = StyleSheet.create({
//     container: {
//         flexDirection: 'row',
//         width: 500,
//         paddingTop: StatusBar.currentHeight,
//         marginHorizontal: 16,
//     },
//     item: {
//         backgroundColor: '#0064a4',
//         padding: 20,
//         marginVertical: 8,
//         maxWidth: '100%',
//         maxHeight: '65%',
//         justifyContent: 'center',
//         flex: 1,
//         flexDirection: 'column',
//         alignItems: 'center',
//     },
//     header: {
//         fontSize: 32,
//         backgroundColor: '#fff',
//         textAlign: 'center',
//     },
//     title: {
//         fontSize: 24,
//         textAlign: 'center',
//         color: '#ffffff',
//     },
//     itemTouchable: {
//         flex: 1,
//         width: '100%',
//         borderRadius: 10,
//         overflow: 'hidden',
//     },
//     box: {
//         borderWidth: 1,
//         justifyContent: 'center',
//         flex: 1,
//         // borderColor: 'black',
//         padding: 20,
//         width: '40%',
//         height: '50%',
//         margin: 10,
//         // borderRadius: 8,
//         // backgroundColor: 'lightgrey',
//     },
// })

// const fetchMenu = async () => {
//     try {
//         const response = await fetch(
//             'http://localhost:5000/receive_data'
//         );

//         return response.json();
//     } catch (error) {
//         console.error(error)
//     }
// }

// export function FoodDisplay({ foodName }: { foodName: string }) {
//     return (
//         <View style={styles.container}>
//             <ScrollView>
//                 <TouchableOpacity
//                     onPress={() => console.log(`pressed ${foodName}`)}
//                     style={[styles.item, styles.itemTouchable]}>
//                     <Text style={styles.title}>{foodName}</Text>
//                 </TouchableOpacity>
//             </ScrollView>
//         </View>
//     );
// }

// export function StationDisplay({ stationName, foods }: { stationName: string, foods: any[] }) {
//     return (
//         <ScrollView>
//             <Text style={styles.header}>{stationName}</Text>
//             {
//                 foods.map((item) => (
//                     <FoodDisplay key={item.foodName} foodName={item.foodName} />
//                 ))
//             }
//         </ScrollView>
//     );
// }

// interface MenuItem {
//     station: string,
//     foods: any[];
// }

// export default function MenuComponent() {
//     const [menu, setMenu] = useState<MenuItem[]>([])

//     useEffect(() => {
//         const fetchData = async () => {
//             try {
//                 const response = await fetch('http://localhost:5000/receive_data');
//                 if (!response.ok) {
//                     throw new Error(`HTTP error! Status: ${response.status}`);
//                 }
//                 const data = await response.json();
//                 console.log(data)
//                 setMenu(data);
//             } catch (error) {
//                 console.error(error);
//             }
//         };

//         fetchData();
//     }, []);

//     return (
//         <ScrollView>
//             {menu.map((item) => <StationDisplay key={item.station} stationName={item.station} foods={item.foods} />)}
//         </ScrollView>
//     )
// }
