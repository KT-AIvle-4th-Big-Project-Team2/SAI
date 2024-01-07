import { drawPolygons } from './DrawPolygons.js';
import { drawSelectedPolygon } from './DrawPolygons_jachigu.js';
import { drawPolygonsForCity } from './DrawPolygons_seoul.js'
import React, { Component } from 'react';
import geoJsonData from './geometry.json';
import geoJsonData_jachigu from './jachigugeojson.json'
import './KakaoMap.css'; // 스타일을 위한 CSS 파일을 가정합니다
import Data from '../assets/서울시 행정동.json';
import seoul from './seoul.json'

function calculatePolygonCenter(geometry) {
    let latSum = 0, lngSum = 0, pointsCount = 0;

    // MultiPolygon의 모든 좌표를 순회
    geometry.coordinates.forEach(polygon => {
        polygon.forEach(ring => {
            ring.forEach(coord => {
                lngSum += coord[0]; // 경도 누적
                latSum += coord[1]; // 위도 누적
                pointsCount += 1;
            });
        });
    });
    
    // 평균 좌표 계산
    return {
        lat: latSum / pointsCount,
        lng: lngSum / pointsCount
    };
}

class KakaoMap extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isMenuOpen: false,
            Gu: '',
            selectedDong: '',
            // ... 기타 상태 변수 ...
        };
        this.polygons = []; // 폴리곤 객체를 저장할 배열 초기화
        // 지역구 및 행정동 데이터 처리
        this.uniqueGuArray = Array.from(new Set(Data.map(item => item.시군구명)));
        this.dongData = Data;
        this.markers = [];  // 마커를 저장할 배열
    }

    addMarker = (position) => {
        // 기존 마커 제거
        this.markers.forEach(marker => marker.setMap(null));
        this.markers = [];

        // 새로운 마커 생성
        const marker = new window.kakao.maps.Marker({
            position: position
        });

        // 새로운 마커 지도에 표시
        marker.setMap(this.map);

        // 마커 배열에 새로운 마커 추가
        this.markers.push(marker);
    }

    toggleMenuModal = () => {
        this.setState((prevState) => ({
            isMenuOpen: !prevState.isMenuOpen,
        }));
    }

    componentDidMount() {
        this.initializeMap();
        
        drawPolygonsForCity(this.map, seoul, "서울특별시", this.polygons);
   
        //drawPolygons(this.map, geoJsonData, this.displayMessage);
        //drawSelectedPolygon(this.map, geoJsonData_jachigu, this.displayMessage, '종로구','사직동')
    }

    initializeMap = () => {
        const mapContainer = this.mapContainer;
        const mapOption = {
            center: new window.kakao.maps.LatLng(37.566535, 126.977969), // 서울의 좌표
            level: 8
        };

        this.map = new window.kakao.maps.Map(mapContainer, mapOption);

        const zoomControl = new window.kakao.maps.ZoomControl();
        this.map.addControl(zoomControl, window.kakao.maps.ControlPosition.RIGHT);

        this.marker = new window.kakao.maps.Marker({
            position: this.map.getCenter()
        });
        
        window.kakao.maps.event.addListener(this.map, 'click', this.handleMapClick);
        window.kakao.maps.event.addListener(this.map, 'dragend', this.handleMapDragEnd);
        window.kakao.maps.event.addListener(this.map, 'zoom_changed', this.handleMapZoomChanged);

        
    }

    handleMapClick = (mouseEvent) => {
        const latlng = mouseEvent.latLng;
        //this.marker.setPosition(latlng);
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

    displayMessage = (message) => {
        this.setState({ message });
    };

    handleGuChange = (event) => {
        this.setState({
            Gu: event.target.value,
            selectedDong: '',
        });
        // 선택한 지역구에 따라 지도 업데이트 로직 추가
    };

    handleDongChange = (event) => {
        this.setState({ selectedDong: event.target.value });
        // 선택한 행정동에 따라 지도 업데이트 로직 추가
    };

    componentDidUpdate(prevProps, prevState) {

        if (prevState.Gu !== this.state.Gu || prevState.selectedDong !== this.state.selectedDong) {
            // features 배열에서 해당 지역구 및 행정동에 해당하는 폴리곤 찾기
            const fullAddress = `서울특별시 ${this.state.Gu} ${this.state.selectedDong}`;
            const polygonFeature = geoJsonData_jachigu.features.find(feature => feature.properties.adm_nm === fullAddress);
            console.log("Current State - Gu:", this.state.Gu, "selectedDong:", this.state.selectedDong);
            console.log("Sample feature data:", geoJsonData_jachigu.features.slice(0, 5));

            if (polygonFeature) {

                // 기존 폴리곤 제거
                this.polygons.forEach(polygon => polygon.setMap(null));
                this.polygons = [];
                const polygonGeometry = polygonFeature.geometry;
                const polygonCenter = calculatePolygonCenter(polygonGeometry);
                console.log("Polygon Center:", polygonCenter);
                
                // 지도의 중심을 폴리곤의 중심으로 이동
                this.map.setCenter(new window.kakao.maps.LatLng(polygonCenter.lat, polygonCenter.lng));

                // 마커가 표시될 위치입니다 
                var markerPosition  = new window.kakao.maps.LatLng(polygonCenter.lat, polygonCenter.lng); 

                // 마커를 생성합니다
                var marker = new window.kakao.maps.Marker({
                position: markerPosition
                });

                // 마커가 지도 위에 표시되도록 설정합니다
                //marker.setMap(this.map);
                this.addMarker(markerPosition);
    
                // 폴리곤 그리기 함수 호출 (이 함수가 지도에 폴리곤을 그리는 로직을 포함한다고 가정)
                // 수정된 drawSelectedPolygon 호출
                drawSelectedPolygon(this.map, geoJsonData_jachigu, this.displayMessage, this.state.Gu, this.state.selectedDong, this.polygons);
               
                console.log("componentDidUpdate called_draw");
                this.map.setCenter(new window.kakao.maps.LatLng(polygonCenter.lat, polygonCenter.lng));
                this.map.setLevel(4); // 지도 레벨을 3으로 설정

            }
        }
        
    }
    
    
    render() {
        // ... 기존 렌더링 코드 ...

        return (
            <div className="map-container">
                <nav className="sidebar">
                    {/* 기존 사이드바 코드 */}
                    {/* 지역구 선택 드롭다운 */}
                    <select value={this.state.Gu} onChange={this.handleGuChange}>
                        <option value="">지역구 선택</option>
                        {this.uniqueGuArray.map((gu) => (
                            <option key={gu} value={gu}>{gu}</option>
                        ))}
                    </select>
                    {/* 행정동 선택 드롭다운 */}
                    {this.state.Gu && (
                        <select value={this.state.selectedDong} onChange={this.handleDongChange}>
                            <option value="">행정동 선택</option>
                            {this.dongData
                                .filter(item => item.시군구명 === this.state.Gu)
                                .map(item => (
                                    <option key={item.읍면동명} value={item.읍면동명}>{item.읍면동명}</option>
                                ))
                            }
                        </select>
                    )}
                    {/* 기타 사이드바 요소 */}
                </nav>
                <div className="map" ref={(ref) => { this.mapContainer = ref; }}></div>
            </div>
        );
    }
}

export default KakaoMap;
