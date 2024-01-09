import { convertCoordinatesToLatLng } from "./convertCoordinatesToLatLng";

// GeoJSON 데이터에서 "CTP_KOR_NM":"서울특별시"에 해당하는 피처만 필터링하는 함수
export const filterFeaturesByCityName = (geoJsonData, cityName) => {
    return geoJsonData.features.filter(feature => feature.properties.CTP_KOR_NM === cityName);
};

// 특정 도시에 대한 폴리곤만 그리는 함수 (폴리곤 저장 배열 추가)
export const drawPolygonsForCity = (map, geoJsonData, cityName, polygonsArray) => {
    const filteredFeatures = filterFeaturesByCityName(geoJsonData, cityName);

    console.log("test")
    filteredFeatures.forEach(feature => {
        const { geometry: { type, coordinates } } = feature;

        if (type === "Polygon" || type === "MultiPolygon") {
            const paths = convertCoordinatesToLatLng(coordinates, type);

            const polygon = new window.kakao.maps.Polygon({
                map: map,
                path: paths,
                strokeWeight: 3,
                strokeColor: '#FFA500',
                strokeOpacity: 0.8,
                fillColor: '#FFA500',
                fillOpacity: 0.3
            });

            // 폴리곤을 polygonsArray에 추가
            polygonsArray.push(polygon);

            // 마우스 이벤트 리스너 (색상 변경)
            window.kakao.maps.event.addListener(polygon, 'mouseover', () => {
                polygon.setOptions({ fillColor: '#0000FF' });
            });

            window.kakao.maps.event.addListener(polygon, 'mouseout', () => {
                polygon.setOptions({ fillColor: '#FFA500' });
            });
        }
    });
};

// 사용 예시
// drawPolygonsForCity(map, geoJsonData, "서울특별시");
