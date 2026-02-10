from abc import ABC, abstractmethod

class PipeLineFactory(ABC):
    @abstractmethod
    def save_file(self):
        pass

    @abstractmethod
    def create_thumbnail(self):
        pass

    @abstractmethod
    def extract_data(self):
        pass

    @abstractmethod
    def create_url(self):
        pass

class Enterprise(ABC):
    @abstractmethod
    def






# 1. 파일 저장
# 2. 썸네일 생성
# 3. 미디어 메타데이터 추출
# 4. 접근 URL 생성

# **🏢 현재 고객사 인프라**
# **🟦 Enterprise 고객**
# **🟩 Startup 고객**
# **🟨 Privacy 고객 (보안 중요)**
