import React, { Component } from 'react';

class KakaoMap extends Component {
    state = {
        message: '' // 지도 관련 메시지를 저장하는 state
    };

    componentDidMount() {
        this.initializeMap();
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
            width: '99vw',
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