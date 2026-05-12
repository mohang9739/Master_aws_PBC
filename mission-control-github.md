# 🚀 Platform Engineer Mission Control - Learning Dashboard

**A complete roadmap to become a Platform Engineer by September 2026**

> This is an interactive dashboard designed to track your journey from zero to professional platform engineer with focus on AWS, Python, Kubernetes, and DevOps.

---

## 📋 Core Courses

| Course | Author | Hours | Period | Resource |
|--------|--------|-------|--------|----------|
| 100 Days of Code: Python | Angela Yu | 60h | Wk 1-4 | [Udemy](https://www.udemy.com/course/100-days-of-code/) |
| Linux Bootcamp 2026 | Andrei Dumitrescu | 28h | Wk 1-4 | [Udemy](https://www.udemy.com/course/master-linux-administration/) |
| AWS SAA-C03 | Stéphane Maarek | 27h | Wk 1-4 | [Udemy](https://www.udemy.com/course/ultimate-aws-certified-solutions-architect-associate-saa-c03/) |
| Docker Mastery | Bret Fisher | 21h | Wk 5-6 | [Udemy](https://www.udemy.com/course/docker-mastery/) |
| Python for DevOps | Sander van Vugt | 23h | Wk 5-7 | [Udemy](https://www.udemy.com/course/python-devops/) |
| HashiCorp Terraform Associate 2026 | Zeal Vora | 14h | Wk 7-9 | [Udemy](https://www.udemy.com/course/terraform-beginner-to-advanced/) |
| Ansible for Absolute Beginner | Mumshad | 3h | Wk 8 | [Udemy](https://www.udemy.com/course/learn-ansible/) |
| GitHub Actions: Complete Guide | Maximilian Schwarzmüller | 8h | Wk 9 | [Udemy](https://www.udemy.com/course/github-actions-the-complete-guide/) |
| CKA Kubernetes Admin | Mumshad | 21h | Wk 10-12 | [Udemy](https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/) |
| AWS DevOps Pro DOP-C02 | Stéphane Maarek | 25h | Wk 13-15 | [Udemy](https://www.udemy.com/course/aws-certified-devops-engineer-professional-hands-on/) |
| Advanced DevSecOps | Hands-on Labs | 14h | Wk 14-15 | [Udemy](https://www.udemy.com/course/advanced-devsecops-real-world-security-for-devops-engineers/) |
| Karpenter Masterclass for Kubernetes | Rajdeep Saha (ex-AWS Principal SA) | 5h | Wk 12 | [Udemy](https://www.udemy.com/course/karpenter-masterclass-for-kubernetes/) |
| Mastering FinOps for Engineers | FinOps Foundation | 4h | Wk 13 | [Udemy](https://www.udemy.com/course/mastering-finops-for-engineers-certification-course/) |

---

## 🔧 DevOps Tools & Skills

### Core Tools (Must Master)
- **Git/GitHub** - Source control · branching · PRs (Wk 1+)
- **Docker** - Containers · images · Compose (Wk 5) | [Udemy: Docker Mastery](https://www.udemy.com/course/docker-mastery/)
- **Kubernetes** - Pods · Deployments · Services (Wk 10) | [Udemy: CKA](https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/)
- **Terraform** - IaC · HCL · modules · state (Wk 7) | [Udemy: Terraform](https://www.udemy.com/course/terraform-beginner-to-advanced/)
- **Ansible** - Playbooks · roles · YAML (Wk 8) | [Udemy: Ansible](https://www.udemy.com/course/learn-ansible/)
- **GitHub Actions** - CI/CD · OIDC · matrix builds · reusable workflows (Wk 9) | [Udemy: GitHub Actions](https://www.udemy.com/course/github-actions-the-complete-guide/)

### Advanced CI/CD
- **GitLab CI/CD** - All-in-one DevOps · .gitlab-ci.yml · DAG pipelines (Wk 9) | [Free: GitLab Docs](https://docs.gitlab.com)
- **Jenkins** - Legacy CI · awareness only · 1hr YouTube (Wk 9)
- **ArgoCD** - GitOps · K8s deploys (Wk 12) | [Free: Viktor Farcic YT](https://www.youtube.com/channel/UCveguEn0YLRmCmr4NToHYfA)
- **Helm** - K8s package manager (Wk 11) | [Udemy: CKA](https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/)
- **Karpenter** - Modern K8s node autoscaling · EKS (Wk 12) | [Udemy: Karpenter](https://www.udemy.com/course/karpenter-masterclass-for-kubernetes/)

### Networking & Infrastructure
- **TCP/IP · DNS · HTTP · eBPF** - Containers = Linux processes (Wk 2-3) | [Free: Julia Evans Zines](https://networkingzine.com)
- **CoreDNS** - K8s in-cluster DNS (Wk 10) | [Free: CoreDNS Docs](https://coredns.io)
- **CNI Plugins** - Cilium/Calico/Flannel (Wk 10) | [Free: Cilium Docs](https://cilium.io)
- **Cilium + Hubble** - eBPF-based CNI · zero-instrumentation observability (Wk 11) | [Free: Cilium Learn](https://cilium.io/learn)
- **HTTP/HTTPS Deep** - TLS handshake · status codes · curl (Wk 2) | [Free: MDN Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP)

### Monitoring & Observability
- **CloudWatch** - AWS metrics · logs · alarms · dashboards (Wk 6+) | [Udemy: SAA+DOP](https://www.udemy.com/course/ultimate-aws-certified-solutions-architect-associate-saa-c03/)
- **AWS X-Ray** - Distributed tracing on AWS (Wk 13) | [Udemy: DOP](https://www.udemy.com/course/aws-certified-devops-engineer-professional-hands-on/)
- **Prometheus** - Pull-based metrics · PromQL · exporters (Wk 14) | [Free: Official Docs](https://prometheus.io)
- **Grafana** - Dashboards · Alertmanager (Wk 14) | [Free: KodeKloud](https://kodekloud.com)
- **Loki** - Log aggregation · LogQL (Wk 14) | [Free: Grafana Docs](https://grafana.com/docs/loki/)
- **Tempo** - Distributed tracing (Wk 14) | [Free: Grafana Docs](https://grafana.com/docs/tempo/)
- **Alertmanager** - Alert routing · silencing (Wk 14) | [Free: Official Docs](https://prometheus.io/docs/alerting/latest/overview/)
- **Jaeger** - Open-source distributed tracing (Wk 14) | [Free: Official Docs](https://www.jaegertracing.io)
- **ELK Stack** - Elasticsearch + Logstash + Kibana (Wk 14) | [Free: YouTube](https://www.youtube.com)
- **OpenTelemetry** - Vendor-neutral instrumentation (Wk 14) | [Free: OpenTelemetry Docs](https://opentelemetry.io)
- **Container Insights** - EKS/ECS monitoring (Wk 13) | [Udemy: DOP](https://www.udemy.com/course/aws-certified-devops-engineer-professional-hands-on/)
- **Thanos** - Prometheus long-term storage (Wk 15) | [Free: Thanos Docs](https://thanos.io)
- **SLOs/SLIs/Error Budgets** - Reliability contracts (Wk 14) | [Free: Google SRE Book](https://sre.google)

### Python & AWS Automation
- **AWS Boto3** - Python AWS SDK (Wk 5) | [Udemy: Python for DevOps](https://www.udemy.com/course/python-devops/)

### Platform Engineering
- **OpenTofu** - Open-source Terraform fork (Wk 7) | [Free: OpenTofu Docs](https://opentofu.org)
- **Devtron** - AI-native K8s management · IDP (Wk 16) | [Free: Devtron](https://devtron.ai)
- **Backstage** - Internal Developer Portal (Wk 16) | [Free: Backstage Docs](https://backstage.io)
- **Kyverno** - K8s-native policy-as-code (Wk 13) | [Free: Kyverno Docs](https://kyverno.io)
- **OPA / Gatekeeper** - Open Policy Agent (Wk 13) | [Free: OPA Docs](https://openpolicyagent.org)
- **Crossplane** - K8s control plane for cloud infra (Wk 16) | [Free: Crossplane Docs](https://crossplane.io)
- **Istio** - Service mesh · mTLS · traffic splitting (Wk 15) | [Free: Istio Docs](https://istio.io)
- **FinOps / Kubecost** - Cloud cost management (Wk 13) | [Udemy: FinOps](https://www.udemy.com/course/mastering-finops-for-engineers-certification-course/)
- **DORA Metrics** - Deploy freq · Lead time · CFR · MTTR (Wk 16) | [Free: Google SRE Book](https://sre.google)
- **Infracost** - PR cost impact (Wk 13) | [Free: Infracost](https://infracost.io)
- **Go (Basics)** - K8s operators · read+understand (Wk 16) | [Free: Go Tour](https://go.dev/tour)
- **Cosign / SBOM** - Supply chain security (Wk 15) | [Free: Sigstore Docs](https://sigstore.dev)
- **Flux** - GitOps alternative to ArgoCD (Wk 12) | [Free: Flux Docs](https://fluxcd.io)

### DevSecOps
- **Trivy** - Container vulnerability scan (Wk 14) | [Udemy: DevSecOps](https://www.udemy.com/course/advanced-devsecops-real-world-security-for-devops-engineers/)
- **Snyk** - Code + dependency scan (Wk 14) | [Udemy: DevSecOps](https://www.udemy.com/course/advanced-devsecops-real-world-security-for-devops-engineers/)
- **SonarQube** - Code quality · SAST (Wk 15) | [Udemy: DevSecOps](https://www.udemy.com/course/advanced-devsecops-real-world-security-for-devops-engineers/)
- **OWASP ZAP** - DAST · runtime scan (Wk 15) | [Udemy: DevSecOps](https://www.udemy.com/course/advanced-devsecops-real-world-security-for-devops-engineers/)
- **Checkov** - IaC scan · Terraform (Wk 14) | [Free: Docs](https://www.checkov.io)
- **tfsec** - Terraform security scan (Wk 14) | [Free: Docs](https://aquasecurity.github.io/tfsec/)
- **HashiCorp Vault** - Secrets management (Wk 15) | [Free: Vault Tutorials](https://www.vaultproject.io/docs)
- **Falco** - K8s runtime security (Wk 15) | [Udemy: DevSecOps](https://www.udemy.com/course/advanced-devsecops-real-world-security-for-devops-engineers/)
- **AWS GuardDuty** - Threat detection (Wk 15) | [Udemy: DOP](https://www.udemy.com/course/aws-certified-devops-engineer-professional-hands-on/)
- **AWS SecurityHub** - Compliance dashboard (Wk 15) | [Udemy: DOP](https://www.udemy.com/course/aws-certified-devops-engineer-professional-hands-on/)
- **AWS KMS** - Key management (Wk 14) | [Udemy: SAA](https://www.udemy.com/course/ultimate-aws-certified-solutions-architect-associate-saa-c03/)
- **IAM Policies** - Least privilege · SCPs (Wk 13) | [Udemy: DOP](https://www.udemy.com/course/aws-certified-devops-engineer-professional-hands-on/)

---

## 💻 Coding Practice

### LeetCode - Arrays & Strings (30+ problems)
- **Week 1-2:** FizzBuzz, Defanging IP, Running Sum, Maximum Wealth
- **Week 3-4:** Reverse String, Palindrome Number, Jewels and Stones
- **Week 5-6:** Single Number, Contains Duplicate, Two Sum, Valid Anagram
- **Week 7-8:** Move Zeroes, Max Consecutive Ones, Missing Number
- **Week 9-10:** Best Time to Buy/Sell Stock, Rotate Array, Valid Parentheses
- **Week 11-12:** Intersection of Arrays, Frequency Count, Find Duplicates
- **Week 13-18:** Top K Frequent, Group Anagrams, Merge Intervals

[View Full LeetCode Pool →](https://leetcode.com)

### HackerRank - Python Track (50+ problems)
- **Basics:** Hello World, If-Else, Arithmetic, Loops, Print Function
- **Functions & Strings:** Write Function, Lists, Comprehensions, String Operations
- **Advanced:** Sets, Collections (Counter, namedtuple, OrderedDict, deque)
- **Regex & Decorators:** Pattern matching, substitution, decorator patterns
- **Complex Challenges:** Phone validation, email validation, word ordering

[View Full HackerRank Track →](https://www.hackerrank.com)

---

## 📊 Timeline at a Glance

```
MAY              JUNE            JULY            AUGUST      SEPT
├─ Python       ├─ Terraform    ├─ K8s          ├─ Security
├─ Linux        ├─ Docker       ├─ CI/CD        ├─ Monitoring
├─ AWS SAA      ├─ Ansible      ├─ ArgoCD       ├─ Wrap-up
│               ├─ GitHub Actions
```

---

## 🎯 Weekly Focus Areas

| Week | Primary Focus | Secondary | Tools to Learn |
|------|---------------|-----------|-----------------|
| 1-2 | Python Basics | Linux | Git, VSCode |
| 3-4 | AWS Fundamentals | Python Advanced | AWS CLI, boto3 |
| 5-6 | Docker | Python DevOps | Docker, ECR |
| 7-8 | Terraform | Ansible | Terraform, State |
| 9 | GitHub Actions | CI/CD Basics | GHA, Workflows |
| 10-12 | Kubernetes | Helm | EKS, kubectl |
| 13-15 | DevOps Advanced | DevSecOps | Monitoring Tools |
| 16-18 | Platform Engineering | Final Projects | IDP, Backstage |
| 19-20 | Portfolio Polish | Interview Prep | Documentation |

---

## 🚀 GitHub Project Structure

```
pbc-platform-engineer/
├── 01-python-basics/          # Python fundamentals + exercises
├── 02-aws-free-tier/          # AWS setup + boto3 scripts
├── 03-terraform-infra/        # Simple VPC + EC2 + S3
├── 04-docker-practice/        # Docker images + Compose
├── 05-simple-k8s/             # Minikube + deployments
├── 06-cicd-pipeline/          # GitHub Actions workflows
├── 07-capstone-project/       # Integrated platform
├── 08-leetcode-solutions/     # Problem solutions
└── 09-hackerrank-solutions/   # HackerRank complete
```

---

## ✅ Success Criteria by September

- ✅ 200+ hours of structured learning
- ✅ 5+ portfolio projects on GitHub
- ✅ 50+ LeetCode problems solved
- ✅ AWS SAA + Terraform certifications
- ✅ CKA Kubernetes basics
- ✅ Complete CI/CD pipeline
- ✅ DevSecOps fundamentals
- ✅ Ready for Platform Engineer interview

---

## 🔗 Quick Links

- [AWS Free Tier](https://aws.amazon.com/free/)
- [Udemy Courses](https://www.udemy.com)
- [LeetCode](https://leetcode.com)
- [HackerRank](https://www.hackerrank.com)
- [GitHub Skills](https://skills.github.com)
- [Docker Hub](https://hub.docker.com)
- [Kubernetes Docs](https://kubernetes.io/docs)
- [Terraform Docs](https://www.terraform.io/docs)
- [Prometheus Docs](https://prometheus.io/docs)
- [Grafana Docs](https://grafana.com/grafana/documentation)

---

## 📝 Notes

- All courses are on **Udemy** (look for sales - usually 80-90% off)
- Free tier resources are prioritized where available
- AWS free tier: **12 months** - watch your spend
- Spend 2-3 hours daily on learning + hands-on practice
- Update this tracking dashboard weekly
- Push all code to GitHub - this is your portfolio

---

**Last Updated:** May 2026  
**Goal Date:** September 1, 2026  
**Status:** 🚀 In Progress
