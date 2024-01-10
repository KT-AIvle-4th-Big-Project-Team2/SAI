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
            isMenu1Open: false,
            isMenu2Open:false,
            isMenu3Open:false,
            isMenu4Open:false,
            isMenu5Open:false,
            selectedMenu: '',
            Gu: '',
            selectedDong: '',
            selectedmarket:'',
            selectedservice:'',
            capital:'',
            buttonStyle: {
                width: '80px', // Set the desired width
                height: '45px', // Set the desired height
                // Add other common styles if needed
            },
            buttonStyle2: {
                width: '125px', // Set the desired width
                height: '52px', // Set the desired height
                // Add other common styles if needed
            },
            
            // ... 기타 상태 변수 ...
        };
        this.polygons = []; // 폴리곤 객체를 저장할 배열 초기화
        // 지역구 및 행정동 데이터 처리
        this.uniqueGuArray = Array.from(new Set(Data.map(item => item.시군구명)));
        this.dongData = Data;
        this.marketData=Data2;
        this.serviceList= ['한식음식점', '커피-음료', '분식전문점', '호프-간이주점', '치킨전문점', '중식음식점', '패스트푸드점', '제과점', '일식음식점', '양식음식점', '편의점', '일반의류', '화장품', '의약품', '일반교습학원', '미용실'];
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

    // toggleMenuModal = () => {
    //     this.setState((prevState) => ({
    //         isMenu1Open: !prevState.isMenu1Open,
    //     }));
    // }

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
        let imageSrc = '';
        let altText='';
    // progress 이미지 설정
        if (this.state.Gu === '') {
            imageSrc = progress0Image;
            altText='진행상태1';
        } else if (this.state.selectedDong==='' &&this.state.isMenu1Open) {
            imageSrc = progress1Image;
            altText='진행상태2'; 
        } else if (this.state.selectedmarket==='' && this.state.isMenu2Open) {
            imageSrc = progress2Image;
            altText='진행상태3';
        } else if (this.state.selectedservice==='' && this.state.isMenu3Open) {
            imageSrc = progress3Image;
            altText='진행상태4';
        } else if (this.state.isMenu4Open) {
            imageSrc = progress4Image;
            altText='진행상태5';
        } else if (this.state.isMenu5Open) {
            imageSrc = progress5Image;
            altText='진행상태6';
        } 
        
        return (
            <div className="map-container">
            
                <nav className={this.state.selectedMenu === '' ? 'startbar' : 'startbar hidden'}>
                    {/* username */}
                    {/* <strong>{this.props.username}님, 반가워요!<br/>창업을 고민하시는 분석 단위를 선택해 주세요.<br/></strong> */}
                    <div style={{marginLeft : 25, marginTop : 25}}>
                    <span style={{fontWeight : 'bold'}}>오진원님, 반가워요!<br/></span> 
                    <span style={{fontWeight : 'bold'}}>창업을 고민하시는 분석 단위를 선택해 주세요.<br/></span> 
                    </div>
                    
                    {/* 행정동 단위로 분석하기 버튼 클릭 시 selectedMenu를 'sidebar1'로 설정 */}
                    <button onClick={() => this.setState({ selectedMenu: 'sidebar1' })}>
                        행정동 단위로 분석하기
                    </button>
                    {/* 상권 단위로 분석하기 버튼 클릭 시 selectedMenu를 'sidebar2'로 설정 */}
                    <button onClick={() => this.setState({ selectedMenu: 'sidebar2' })}>
                        상권 단위로 분석하기
                    </button>
                </nav>
                
                {/* 상권 단위 - sidebar2 */}
                {this.state.selectedMenu === 'sidebar2' && (
                    <nav className="sidebar2">
                        {/* 뒤로가기 버튼: 지역구 선택창에서 단위분석 선택창으로 이동 */}
                        {!this.state.Gu && (
                            <button onClick={() => this.handleBackButtonClick()} className="back-button">
                                <img src={backImage} alt="뒤로가기" style={{ width: '22px', height: '23px' }} />
                            </button>
                        )}

                        {/* 뒤로가기 버튼2: 행정동 선택창에서 지역구 선택창으로 이동 */}
                        {this.state.Gu && !this.state.selectedDong && (
                            <button onClick={() => this.handleBackButtonClick2()} className="back-button">
                                <img src={backImage} alt="뒤로가기" style={{ width: '22px', height: '23px' }} />
                            </button>
                        )}
                        {/* 뒤로가기 버튼3: 상권 선택창에서 행정동 선택창으로 이동 */}
                        {this.state.Gu && this.state.selectedDong &&!this.state.selectedmarket  && (
                            <button onClick={() => this.handleBackButtonClick3()} className="back-button">
                                <img src={backImage} alt="뒤로가기" style={{ width: '22px', height: '23px' }} />
                            </button>
                        )}
                        {/* 뒤로가기 버튼4: 업종 선택창에서 행정동 선택창으로 이동 */}
                        {this.state.Gu && this.state.selectedDong &&this.state.selectedmarket&&!this.state.selectedservice && (
                            <button onClick={() => this.handleBackButtonClick4()} className="back-button">
                                <img src={backImage} alt="뒤로가기" style={{ width: '22px', height: '23px' }} />
                            </button>
                        )}
                        {/* 뒤로가기 버튼5: 자본금 입력창에서 업종 선택창으로 이동 */}
                        {this.state.Gu && this.state.selectedDong &&this.state.selectedmarket&&this.state.selectedservice && (
                            <button onClick={() => this.handleBackButtonClick5()} className="back-button">
                                <img src={backImage} alt="뒤로가기" style={{ width: '22px', height: '23px' }} />
                            </button>
                        )}
                        <div className="additional-text">
                            <img src={imageSrc} alt={altText} />
                            <strong>
                                {this.state.Gu === '' ? '어느 지역구에서 창업하시는지 알려주세요' : 
                                this.state.selectedDong=== '' ? '어느 행정동에서 창업하시는지 알려주세요' :
                                this.state.selectedmarket=== '' ? '어떤 상권에서 창업하시는지 알려주세요':
                                this.state.selectedservice=== ''? '어떤 업종으로 창업하시는지 알려주세요 ':
                                '자본금으로'}
                            </strong>
                        </div>

                        {/* 지역구 선택 버튼 */}
                        {this.state.Gu === ''&&  this.uniqueGuArray.map((gu) => (
                            <button
                                key={gu}
                                onClick={() => {
                                    this.handleGuChange({ target: { value: gu } });
                                    this.setState({ isMenu1Open: true });
                                }}
                                style={this.state.buttonStyle}
                            >
                                {gu}
                            </button>
                        ))}

                        {/* 행정동 선택 버튼 */}
                        {this.state.selectedDong==='' &&this.state.isMenu1Open && this.dongData
                            .filter(item => item.시군구명 === this.state.Gu)
                            .map(item => (
                            <button
                                key={item.읍면동명}
                                onClick={() => {
                                    this.handleDongChange({ target: { value: item.읍면동명 } });
                                    // 행정동 선택 후 행정동 버튼들을 숨김
                                    this.setState({ isMenu2Open:true });
                                }}
                                style={this.state.buttonStyle}
                            >
                                {item.읍면동명}
                            </button>
                        ))}
                        {/* 상권 선택 버튼 */}
                        {this.state.selectedmarket==='' && this.state.isMenu2Open && this.marketData
                            .filter(item => item.행정동_코드_명 === this.state.selectedDong)
                            .map(item => (
                            <button
                                key={item.상권_코드_명}
                                onClick={() => {
                                    this.handleMarketChange({ target: { value: item.상권_코드_명 } });
                                    // 상권 선택 후 상권 버튼들을 숨김
                                    this.setState({isMenu3Open:true });
                                }}
                                style={this.state.buttonStyle2}
                            >
                                {item.상권_코드_명}
                            </button>
                        ))}

                        {/* 서비스 업종 선택 버튼 */}
                        {this.state.selectedmarket && this.state.selectedservice === '' && this.state.isMenu3Open && this.serviceList.map((service) => (
                            <button
                                key={service}
                                onClick={() => {
                                    this.handleServiceChange(service);
                                    this.setState({ isMenu4Open: true });
                                }}
                                style={{ width:'90px',height:'90px',display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center',margin: '3px' }}
                            >
                                <img
                                    src={getServiceIconPath(service)}
                                    alt={service}
                                    // 업종 버튼 이미지 스타일 조정
                                    style={{ width: '35px', height: '35px',marginTop:'7px' }}
                                />
                                <span>{service}</span>
                            </button>
                        ))}

                        {/* 자본금 입력 받고 창업도우미 시작 버튼 */}
                        {this.state.selectedmarket && this.state.isMenu4Open && (<strong>얼마를 생각하시는지 알려주세요</strong>)}
                        {this.state.selectedmarket && this.state.isMenu4Open && (
                            <form onSubmit={this.handleCapitalSubmit} style={{marginTop:'20px',display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                            {/* 자본금 입력창 */}
                            <input
                                type="text"
                                placeholder="₩ 자본금 입력 (만원)"
                                value={this.state.capital}
                                onChange={(e) => this.setState({ capital: e.target.value })}
                                style={{
                                    border: 'none',
                                    borderBottom: '1px solid #6A85E6', // Blue color for the underline
                                    padding: '5px', // Adjust padding as needed
                                    marginBottom: '10px' // Adjust margin as needed
                                }}
                            />
                            {/* SAI 창업 도우미 시작하기 버튼 */}
                            <button type="submit" className="sai-button" style={{marginTop:'20px'}}>
                                SAI 창업 도우미 시작하기
                            </button>
                        </form>
                        )}
                    </nav>)
                }

                <div className="map" ref={(ref) => { this.mapContainer = ref; }}></div>
            </div>
        );
    }

    handleBackButtonClick = () => {
        // 뒤로가기 버튼 클릭 시, 분석단위 선택으로 돌아가기
        this.setState({
            selectedMenu:'',
        });
    };

    handleBackButtonClick2 = () => {
        // 뒤로가기 버튼 클릭 시, 지역구 선택으로 돌아가기
        this.setState({
            Gu: '',
        });
    };
    handleBackButtonClick3 = () => {
        // 뒤로가기 버튼 클릭 시, 행정동 선택으로 돌아가기
        this.setState({
            selectedDong: '',
        });
    };
    handleBackButtonClick4 = () => {
        // 뒤로가기 버튼 클릭 시, 상권 선택으로 돌아가기
        this.setState({
            selectedmarket: '',
        });
    };
    handleBackButtonClick5 = () => {
        // 뒤로가기 버튼 클릭 시, 업종 선택으로 돌아가기
        this.setState({
            selectedservice: '',
        });
    };

    
    // 지역구 선택 이벤트 핸들러
    handleGuChange = (event) => {
        this.setState({
            Gu: event.target.value,
            selectedDong: '',
        });
    };

    // 행정동 선택 이벤트 핸들러
    handleDongChange = (event) => {
        this.setState({ selectedDong: event.target.value });
    };

    // 상권 선택 이벤트 핸들러
    handleMarketChange = (event) => {
        this.setState({ selectedmarket: event.target.value });
    };

    // 서비스 업종 선택 이벤트 핸들러
    handleServiceChange = (service) => {
        this.setState({selectedservice:service});
    };
    // 자본금 입력 폼 제출 이벤트 핸들러
    handleCapitalSubmit = (event) => {
        event.preventDefault();
        // SAI 창업 도우미 시작 함수 호출
        this.startSAIHelper();
        this.setState({ capital: '' });
    };
    // SAI 창업 도우미 시작 함수 구현
    startSAIHelper() {
    // this.state.capital을 이용하여 자본금에 관련된 로직을 처리
    const capitalValue = parseInt(this.state.capital, 10);

    // 예를 들어, 자본금이 유효한지 확인하는 로직 등을 추가
    if (isNaN(capitalValue) || capitalValue <= 0) {
        alert('유효한 자본금을 입력하세요.');
        return;
    }

    // 자본금에 따른 추가 로직 구현...

    console.log('선택된 지역구:', this.state.Gu);
    console.log('선택된 행정동:', this.state.selectedDong);
    console.log('선택된 상권:', this.state.selectedmarket);
    console.log('선택된 서비스 업종:', this.state.selectedservice);
    console.log('입력된 자본금:', capitalValue);

    // 추가로 필요한 로직이 있다면 여기에 추가합니다.
    // 예를 들어, 다음 단계로 진행하는 코드를 추가할 수 있습니다.
    this.setState({ isMenu5Open: true }); // 다음 단계를 열도록 상태 업데이트
    }

}

export default KakaoMap;
