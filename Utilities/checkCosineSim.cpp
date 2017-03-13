//To check the correctness of comparison by Cosine similarity
#include <bits/stdc++.h>
using namespace std;

#define wl(n) while(n--)
#define fr(i,a,b) for(i=a;i<b;i++)

#define bitcnt(x) __builtin_popcount(x)
#define mem(a,i) memset(a,i,sizeof(a))
typedef pair<int,int> ii;
#define mp make_pair
#define ll long long
#define MOD 1000000007
#define pb push_back
#define nl printf("\n")
#define INF (1LL<<52)

bool debug = true;
int main()
{
	int n,i,a;
	double b;
	string c;
	vector<pair<int,pair<double,string> > >v;
	cin>>n;
	fr(i,0,n)
	{
		cin>>a>>b>>c;
		v.pb(mp(a,mp(b,c)));
	}
	sort(v.begin(),v.end());
    nl;nl;
    cout<<v.size();nl;
	fr(i,0,v.size())
	{
		cout<<v[i].first<<" "<<v[i].second.first<<" "<<v[i].second.second<<endl;
	}
	return 0;
}

