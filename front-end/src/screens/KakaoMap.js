import React, { Component } from 'react';
import geoJsonData from './converted_geojson_file.json';

class KakaoMap extends Component {
    state = {
        message: '' // 지도 관련 메시지를 저장하는 state
    };

    componentDidMount() {
        this.initializeMap();
        this.drawPolygons();
    }

    drawPolygons = () => {
        const map = this.map; // KakaoMap 인스턴스
    
        geoJsonData.features.forEach(feature => {
            const { geometry: { type, coordinates }, properties } = feature; // properties를 feature에서 직접 추출
    
            if (type === "Polygon" || type === "MultiPolygon") {
                // 상권 영역의 좌표를 LatLng 객체로 변환
                const paths = this.convertCoordinatesToLatLng(coordinates, type);
    
                const polygon = new window.kakao.maps.Polygon({
                    map: map,
                    path: paths,
                    // 상권 폴리곤 스타일 설정
                    strokeWeight: 3,
                    strokeColor: '#FFA500', // 상권 폴리곤의 선 색상
                    strokeOpacity: 0.8,
                    fillColor: '#FFA500', // 상권 폴리곤의 채움 색상
                    fillOpacity: 0.3 // 상권 폴리곤의 채움 투명도
                });
    
                // 마우스 오버 이벤트 핸들러
                window.kakao.maps.event.addListener(polygon, 'mouseover', () => {
                    polygon.setOptions({ fillColor: '#0000FF' }); // 마우스 오버 시 색상 변경
                    if (properties && properties.TRDAR_CD_N) {
                        this.displayMessage(`상권 이름: ${properties.TRDAR_CD_N}`); // 상권 이름 표시
                    }
                });
    
                // 마우스 아웃 이벤트 핸들러
                window.kakao.maps.event.addListener(polygon, 'mouseout', () => {
                    polygon.setOptions({ fillColor: '#FFA500' }); // 원래 색상으로 변경
                    this.displayMessage(''); // 메시지 지우기
                });
            }
        });
    }
    
    
    
    // 좌표를 LatLng 객체로 변환
    convertCoordinatesToLatLng = (coordinates, type) => {
        let paths = [];

        if (type === "Polygon") {
            paths = coordinates[0].map(coord => new window.kakao.maps.LatLng(coord[1], coord[0]));
        } else if (type === "MultiPolygon") {
            coordinates.forEach(polygon => {
                const path = polygon[0].map(coord => new window.kakao.maps.LatLng(coord[1], coord[0]));
                paths.push(path);
            });
        }

        return paths;
    }

    initializeMap = () => {
        const mapContainer = this.mapContainer;
        const mapOption = {
            center: new window.kakao.maps.LatLng(37.566535, 126.977969), // 서울의 좌표
            level: 3
        };

        this.map = new window.kakao.maps.Map(mapContainer, mapOption);

        const zoomControl = new window.kakao.maps.ZoomControl();
        this.map.addControl(zoomControl, window.kakao.maps.ControlPosition.RIGHT);

        this.marker = new window.kakao.maps.Marker({
            position: this.map.getCenter()
        });
        this.marker.setMap(this.map);

        window.kakao.maps.event.addListener(this.map, 'click', this.handleMapClick);
        window.kakao.maps.event.addListener(this.map, 'dragend', this.handleMapDragEnd);
        window.kakao.maps.event.addListener(this.map, 'zoom_changed', this.handleMapZoomChanged);
    }

    handleMapClick = (mouseEvent) => {
        const latlng = mouseEvent.latLng;
        this.marker.setPosition(latlng);
        this.displayMessage(`클릭한 위치: 위도 ${latlng.getLat()}, 경도 ${latlng.getLng()}`);
    };

    handleMapDragEnd = () => {
        const latlng = this.map.getCenter();
        this.displayMessage(`지도 중심좌표: 위도 ${latlng.getLat()}, 경도 ${latlng.getLng()}`);
    };

    handleMapZoomChanged = () => {
        const level = this.map.getLevel();
        this.displayMessage(`지도 레벨: ${level}`);
    };

    toggleMapType = (type) => {
        const mapTypeId = window.kakao.maps.MapTypeId[type.toUpperCase()];
        this.map.removeOverlayMapTypeId(mapTypeId);
        const checkBox = document.getElementById(`chk${type.charAt(0).toUpperCase() + type.slice(1)}`);
        if (checkBox && checkBox.checked) {
            this.map.addOverlayMapTypeId(mapTypeId);
        }
    };

    displayMessage = (message) => {
        this.setState({ message });
    };

    render() {
        const mapStyle = {
            width: '65vw',
            height: '80vh'
        };

        return (
            
            <div>
                <div ref={(ref) => { this.mapContainer = ref; }} style={mapStyle}></div>
                <div className="button">
                    <label><input type="checkbox" id="chkTraffic" onChange={() => this.toggleMapType('traffic')} /> 교통정보</label>
                    <label><input type="checkbox" id="chkRoadview" onChange={() => this.toggleMapType('roadview')} /> 로드뷰 도로정보</label>
                    <label><input type="checkbox" id="chkTerrain" onChange={() => this.toggleMapType('terrain')} /> 지형정보</label>
                    <label><input type="checkbox" id="chkUseDistrict" onChange={() => this.toggleMapType('use_district')} /> 지적편집도</label>
                </div>
                <p><em>지도 기능을 테스트 해보세요!</em></p>
                <p>{this.state.message}</p>
            </div>
        );
    }
}

export default KakaoMap;
