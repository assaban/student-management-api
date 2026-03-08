# Assignment 1 Completion Report
**Tutorial:** RESTful Services, Docker, and Kubernetes  
**Student:** Mohsin Assaban (assaban)  
**Repository:** https://github.com/assaban/student-management-api  
**Date Completed:** March 8, 2026

## Executive Summary

This assignment involved building a complete RESTful API for student management, containerizing it with Docker, establishing CI/CD pipelines, and deploying to Kubernetes. The implementation demonstrates the full DevOps lifecycle from development to deployment.

## Tutorial Checklist

### Phase 1: Prerequisites ✅
- [x] GitHub account (assaban)
- [x] Docker Hub account (mohssinassaban)
- [x] SwaggerHub account
- [x] Docker installed
- [x] Development environment ready

### Phase 2: API Design ✅
- [x] Created OpenAPI 3.0 specification in SwaggerHub
- [x] Defined Student schema (student_id, first_name, last_name, grade_records)
- [x] Defined GradeRecord schema (subject_name, grade with min:0, max:10)
- [x] Implemented CRUD endpoints:
  - GET /student (list all students)
  - POST /student (create student)
  - GET /student/{student_id} (get one student)
  - DELETE /student/{student_id} (delete student)

### Phase 3: Implementation ✅
- [x] Generated Python Flask server stubs from OpenAPI
- [x] Implemented service layer (swagger_server/service/student_service.py)
  - TinyDB for lightweight file-based persistence
  - Complete CRUD operations
- [x] Connected controllers to service layer
- [x] Layered architecture (Controllers → Service → Database)

### Phase 4: Version Control ✅
- [x] Initialized Git repository
- [x] Created public GitHub repository
- [x] Regular commits with descriptive messages
- [x] Proper .gitignore configuration

### Phase 5: Containerization ✅
- [x] Created Dockerfile with Python 3.9-alpine base
- [x] Optimized multi-stage build process
- [x] Configured for port 8080 exposure
- [x] Image published to Docker Hub: mohssinassaban/student_service

### Phase 6: CI/CD ✅
- [x] Created Postman test collection
- [x] Configured GitHub Actions workflow
  - Automated testing on push
  - Docker build and push on successful tests
- [x] Configured Docker Hub secrets (REGISTRY_USERNAME, REGISTRY_PASSWORD)
- [x] Pipeline tested and working

### Phase 7: Kubernetes ✅
- [x] Created K8s deployment manifest (k8s/student_service.yaml)
  - 2 replicas for high availability
  - NodePort service (port 30726)
  - Resource requests and limits defined
- [x] Ready for Minikube deployment

### Phase 8: Exercises ✅
- [x] Exercise 3.2: Added average_grade endpoint
  - GET /student/{student_id}/average_grade
  - Calculates average of all grade records
  - Returns 404 if student not found or has no grades

## Technical Implementation Details

### API Endpoints

| Method | Path | Description | Request | Response |
|--------|------|-------------|---------|----------|
| GET | /student | List all students | - | Array of Student objects |
| POST | /student | Add new student | Student object | student_id (number) |
| GET | /student/{id} | Get student by ID | - | Student object |
| DELETE | /student/{id} | Delete student | - | Success message |
| GET | /student/{id}/average_grade | Get average grade | - | Average (number) |

### Data Models

**Student Object:**
```json
{
  "student_id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "grade_records": [
    {
      "subject_name": "Mathematics",
      "grade": 8.5
    }
  ]
}
```

**GradeRecord Object:**
```json
{
  "subject_name": "Mathematics",
  "grade": 8.5
}
```

### Architecture

```
┌─────────────────┐
│  Swagger UI     │
│  (Frontend)     │
└────────┬────────┘
         │
         │ HTTP/JSON
         │
┌────────▼────────────────────┐
│  Flask/Connexion            │
│  (Controllers)              │
│  - default_controller.py    │
└────────┬────────────────────┘
         │
         │ Function Calls
         │
┌────────▼────────────────────┐
│  Service Layer              │
│  - student_service.py       │
│  (Business Logic)           │
└────────┬────────────────────┘
         │
         │ Query/Insert
         │
┌────────▼────────────────────┐
│  TinyDB                     │
│  (students_db.json)         │
└─────────────────────────────┘
```

### Key Technologies Used

- **OpenAPI 3.0**: API specification and documentation
- **Python 3.9**: Programming language
- **Flask 2.2.5**: Web framework
- **Connexion 2.14.1**: OpenAPI integration
- **TinyDB 4.7.0**: Document-oriented database
- **Docker**: Containerization
- **Kubernetes**: Orchestration
- **GitHub Actions**: CI/CD automation
- **Postman/Newman**: API testing

## Learning Outcomes

### 1. RESTful API Design
**Concept Learned:** API-first design using OpenAPI specification  
**Key Insight:** Defining the API contract before implementation ensures consistency and enables auto-generated documentation

**Example:** The OpenAPI spec serves as both:
- Contract between frontend and backend teams
- Auto-generated Swagger UI for testing
- Validation schema for request/response objects

### 2. Layered Architecture
**Concept Learned:** Separation of concerns (Controller → Service → Data)  
**Key Insight:** Each layer has a single responsibility, making code testable and maintainable

**Example:**
- **Controller**: HTTP request/response handling
- **Service**: Business logic (average calculation)
- **Data**: Persistence operations

### 3. Containerization
**Concept Learned:** Docker packaging ensures environment consistency  
**Key Insight:** "Works on my machine" problem solved - same container runs identically everywhere

**Example:** The Docker image contains:
- Python 3.9 runtime
- All dependencies (Flask, Connexion, TinyDB)
- Application code
- Configuration

### 4. Kubernetes Orchestration
**Concept Learned:** K8s manages container lifecycle, scaling, and networking  
**Key Insight:** Declarative configuration (YAML) describes desired state; K8s maintains it

**Example:** With 2 replicas:
- If one pod crashes, K8s automatically recreates it
- Load balanced across both pods
- Zero-downtime deployments possible

### 5. CI/CD Automation
**Concept Learned:** GitHub Actions automates build, test, deploy pipeline  
**Key Insight:** Every commit triggers automated quality checks, preventing broken code from reaching production

**Pipeline Flow:**
```
git push → GitHub Actions → Run Tests → Build Docker → Push to Docker Hub
```

## Challenges and Solutions

### Challenge 1: Flask/Connexion Version Compatibility
**Problem:** Generated code expected older Flask version, got AttributeError with Flask 2.3+  
**Solution:** Pinned Flask to 2.2.5 in requirements.txt  
**Learning:** Always specify exact dependency versions in production systems

### Challenge 2: Function Naming Conflicts
**Problem:** Controller function `get_average_grade()` conflicted with service import `get_average_grade`  
**Solution:** Changed from `from ... import get_average_grade` to `from ... import student_service`, then called `student_service.get_average_grade()`  
**Learning:** Module imports prevent naming conflicts and improve code organization

### Challenge 3: Kubernetes Resource Configuration
**Problem:** Needed to understand resource requests vs limits  
**Solution:** Researched K8s resource management:
- **Requests**: Guaranteed resources (used for scheduling)
- **Limits**: Maximum allowed (prevents resource hogging)  
**Learning:** Proper resource configuration prevents cluster instability

## Code Quality Metrics

- **Test Coverage**: Postman tests cover all CRUD endpoints + average_grade
- **Code Organization**: Clear separation of controllers, services, models
- **Documentation**: OpenAPI spec provides comprehensive API documentation
- **Error Handling**: All endpoints return appropriate HTTP status codes
- **Resource Management**: K8s limits prevent resource exhaustion

## Deployment Instructions

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run server
python -m swagger_server

# Access API
http://localhost:8080/tutorial/1.0.0/ui/
```

### Docker
```bash
# Build image
docker build -t mohssinassaban/student_service .

# Run container
docker run -p 8080:8080 mohssinassaban/student_service
```

### Kubernetes (Minikube)
```bash
# Start Minikube
minikube start --addons=ingress,ingress-dns,metrics-server

# Deploy application
kubectl apply -f k8s/student_service.yaml

# Get Minikube IP
minikube ip

# Access application
http://<MINIKUBE_IP>:30726/tutorial/1.0.0/ui/
```

## Repository Structure

```
student-management-api/
├── .github/
│   └── workflows/
│       └── main.yml                 # GitHub Actions CI/CD
├── k8s/
│   └── student_service.yaml         # Kubernetes manifests
├── postman/
│   ├── collection.json              # API tests
│   └── environment.json             # Test environment
├── swagger_server/
│   ├── controllers/
│   │   └── default_controller.py    # API endpoints
│   ├── models/
│   │   ├── student.py               # Student model
│   │   └── grade_record.py          # GradeRecord model
│   ├── service/
│   │   └── student_service.py       # Business logic
│   └── swagger/
│       └── swagger.yaml             # OpenAPI definition
├── Dockerfile                       # Container configuration
├── requirements.txt                 # Python dependencies
├── WORK_LOG.md                      # Development log
└── README.md                        # Project documentation
```

## Next Steps

For future enhancements:
1. **Database Migration**: Replace TinyDB with PostgreSQL for production
2. **Authentication**: Add JWT-based authentication
3. **Monitoring**: Implement Prometheus metrics
4. **Logging**: Structured logging with ELK stack
5. **Rate Limiting**: Prevent API abuse
6. **Caching**: Redis for frequently accessed data

## Conclusion

This assignment successfully demonstrated the complete DevOps lifecycle:
- **Plan**: OpenAPI specification
- **Develop**: Python Flask implementation
- **Build**: Docker containerization
- **Test**: Automated Postman tests
- **Deploy**: Kubernetes orchestration
- **Monitor**: Ready for observability tools

The implementation follows industry best practices and is production-ready with minor enhancements (database upgrade, authentication, monitoring).

**Key Takeaway:** Modern software delivery requires automation at every stage. The investment in CI/CD infrastructure pays off through faster, more reliable deployments.
