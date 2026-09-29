<template>
	<BaseLayout :pageTitle="__('Leaves & Holidays')">
		<template #body>
			<div class="flex flex-col items-center mt-5 mb-7 py-4">
				<LeaveBalance />

				<div class="flex flex-col gap-6 mt-5 px-4 w-full">
					<router-link
						:to="{ name: 'LeaveApplicationFormView' }"
						v-slot="{ navigate }"
					>
						<Button
							@click="navigate"
							variant="solid"
							class="py-4 text-base w-full !bg-[#D4AF37] !text-[#051E24] !font-bold rounded-xl shadow-lg border-none hover:!bg-amber-400 transition cursor-pointer"
							style="background: linear-gradient(135deg, #E6CA65 0%, #D4AF37 50%, #B8860B 100%); color: #051E24;"
						>
							<template #prefix>
								<FeatherIcon name="plus-circle" class="w-5 h-5 mr-1" />
							</template>
							{{ __("Request a Leave") }}
						</Button>
					</router-link>
					<div>
						<div class="text-base sm:text-lg text-white font-bold tracking-tight mb-1 px-1">{{ __('Recent Leaves') }} </div>
						<RequestList
							:component="markRaw(LeaveRequestItem)"
							:items="myLeaves.data"
							:addListButton="true"
							listButtonRoute="LeaveApplicationListView"
						/>
					</div>
					<Holidays />
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { markRaw } from "vue"
import { Button, FeatherIcon } from "frappe-ui"

import BaseLayout from "@/components/BaseLayout.vue"
import LeaveBalance from "@/components/LeaveBalance.vue"
import RequestList from "@/components/RequestList.vue"
import LeaveRequestItem from "@/components/LeaveRequestItem.vue"
import Holidays from "@/components/Holidays.vue"

import { myLeaves } from "@/data/leaves"
</script>
