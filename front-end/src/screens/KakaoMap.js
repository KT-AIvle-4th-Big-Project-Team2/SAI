import { drawPolygons } from './DrawPolygons.js';
import React, { Component } from 'react';
import geoJsonData from './geometry.json';
import './KakaoMap.css'; // 스타일을 위한 CSS 파일을 가정합니다


class KakaoMap extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isMenuOpen: false, // 메뉴 모달이 열려있는지 여부를 관리
        };
    }

    toggleMenuModal = () => {
        this.setState((prevState) => ({
            isMenuOpen: !prevState.isMenuOpen,
        }));
    }

    componentDidMount() {
        this.initializeMap();
        drawPolygons(this.map, geoJsonData, this.displayMessage);
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

    displayMessage = (message) => {
        this.setState({ message });
    };

    render() {
        // 메뉴의 상태에 따라 메뉴 클래스를 동적으로 추가/제거
        const menuClass = this.state.isMenuOpen ? 'menu-popup open' : 'menu-popup';

        return (
            <div className="map-container">
                <nav className="sidebar">
                    <text className="title">뜨는 상권</text>
                    <div className="menu-container">
                        <div className="menu-button" onClick={this.toggleMenu}>
                            메뉴 1
                        </div>
                        <div className={menuClass} id="menu-popup">
                            {/* 스크롤바를 활용하기 위한 스타일 추가 */}
                            <div className="menu-items" style={{ maxHeight: '400px', overflowY: 'auto' }}>
                                <button className="menu-item">메뉴 항목 1</button>
                                <button className="menu-item">메뉴 항목 2</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>
                                <button className="menu-item">메뉴 항목 3</button>


                                {/* 더 많은 메뉴 항목을 추가하세요 */}
                            </div>
                        </div>
                    </div>

                    <div className="status">
                        <p>{this.state.message}</p>
                    </div>
                </nav>
                <div className="map" ref={(ref) => { this.mapContainer = ref; }}></div>
            </div>
        );
    }
}

export default KakaoMap;
